import os
import re

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash


from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd
#to configure email

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    data=db.execute("SELECT * FROM users WHERE id = ?",session["user_id"])
    rows = db.execute("SELECT symbol, shares FROM portfolio WHERE user_id = ? GROUP BY symbol",session["user_id"])
    owned_cash = data[0]["cash"]

    if len(rows) == 0:
        rows = None
    else:
        total_share_price = 0
        for row in rows: #pobieramy wiersz

            share = lookup(row["symbol"])#pobieramy dane na temat tego symbolu
            row["share_price"]=share["price"]#zapisujemy cene tego symbolu
            row["total_share_price"]=share["price"] * row["shares"]#cena całkowiata akcji danej firmy

            total_share_price += row["total_share_price"]
            total = owned_cash+total_share_price

    if rows != None:
        return render_template("index.html",owned_cash=owned_cash,total_share_price=total_share_price,total=total,rows=rows)
    else:
        return render_template("index.html",owned_cash = owned_cash,total=owned_cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":

        if not request.form.get("symbol"):

            return apology("missing symbol")
        if not request.form.get("shares"):

            return apology("you can't buy 0 shares")
        if request.form.get("shares").isdigit() == False:

            return apology("You cant buy negative index if actions")

        if lookup(request.form.get("symbol")) == None: #jeśli dany symbol nie istnieje bo np źle został napisany zwróc apology

            return apology("This symbol dosent exist")

        shares = float(request.form.get("shares"))#pobieramy ile akcji chce user kupić
        rows = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])#pobieramy ile pieniędzy user ma
        symbol = lookup(request.form.get("symbol"))
        shares_price = symbol["price"]#pobieramy cene danej akcji
        money = rows[0]["cash"]

        if (shares*shares_price)>money:
            return apology("You haven't enough money")

        else:
            db.execute("INSERT INTO buy2 (user_id,company,symbol,shares,price,type) VALUES (?,?,?,?,?,?)",session["user_id"],symbol["name"],symbol["symbol"],shares,symbol["price"],"buy")#Dodajemy do bazy danych z historią nowy wiersz tyou transakcji

            x=db.execute("SELECT symbol FROM portfolio WHERE user_id=? AND symbol = ?",session["user_id"],symbol["symbol"])#sprawdzamy czy użytkownik już wcześniej kupił akcje tej firmy
            if len(x)<=0:
                total = shares*shares_price
                db.execute("INSERT INTO portfolio (user_id,shares,total,symbol) VALUES (?,?,?,?)",session["user_id"],shares,total,symbol["symbol"])#jeśłi nie ma wierzsza to tworzymy nowy na temat akcji danej firmy
            else:#jeśli user ma już akcje danych firmy to aktualizujemy jego portfolio
                update = db.execute("SELECT * FROM portfolio WHERE user_id=? AND symbol=?",session["user_id"],symbol["symbol"])#pobieramy dane z jego konta w portfolio
                shares_new = shares + update[0]["shares"]
                total_new = update[0]["total"] + (shares*shares_price)
                db.execute("UPDATE portfolio SET shares=? ,total=? WHERE user_id=? AND symbol=?",shares_new,total_new,session["user_id"],symbol["symbol"])

            money = money - (shares*shares_price)#odejmuemy ceny zakupionych akcji od hajsy użytkowanika
            db.execute("UPDATE users SET cash = ? WHERE id = ?",money,session["user_id"])
            flash("Bought")

            return redirect ("/")



    return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    rows = db.execute("SELECT transacted,company,symbol,shares,price,type FROM buy2 WHERE user_id = ?",session["user_id"])
    return render_template("history.html",rows=rows)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = lookup(request.form.get("symbol"))

        if symbol == None:
            return apology("Invalid Symbol")
        return render_template("quoted.html",symbol=symbol)

    return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("Set Username")
        if not request.form.get("password"):
            return apology("Set password")
        if not request.form.get("confirmation"):
            return apology("Repeat Password")
        if request.form.get("confirmation") != request.form.get("password"):
            return apology("Password not match")

        data=db.execute("SELECT * FROM users WHERE username = ?",request.form.get("username"))
        password = request.form.get("password")
        if len(data) > 0: #czyli jeśli obiekt istniej czyli jeśli istnieje dany użytkowanik
            return apology("This name alredy Taken")
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        pat = re.compile(reg)
        match = re.search(pat,password)
        if match:

            db.execute("INSERT INTO users (hash,cash,username)  VALUES (?,?,?)",generate_password_hash(request.form.get("password")),10000,request.form.get("username"))
            flash("you sucessfuly registred")
            return redirect("/")
        else:



            flash("you dont achive conditions")
            return render_template("register.html")





    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    symbols = db.execute("SELECT symbol FROM portfolio WHERE user_id = ?",session["user_id"])
    control=0
    if request.method == "POST":

        if not request.form.get("symbol") or not request.form.get("shares"):#sprawdzamy czy wypełniliśy wszystkie pola
            return apology("You have to fill the form")

       #pobieramy wszystie symbole


        if len(symbols)<=0:
            return apology("You Havent any Stocks")
        for symbol in symbols:


            if symbol["symbol"] == request.form.get("symbol"):#kurwa czemu nie działa?
                control=1

                break #sprawdzamy czy dany symbol istnieje

        if control == 0:
            return apology("you havent stocks of this company")





        shares = db.execute("SELECT shares FROM portfolio WHERE symbol = ? AND user_id=?",request.form.get("symbol"),session["user_id"])#pobieramy liczbę danych akcji danej firmy
        if int(request.form.get("shares"))> int(shares[0]["shares"]):# sprawdzamy czy użytkownik ma wystraczjącą ilość akcji
            return apology("You dont have as much shares")

        share=int(shares[0]["shares"])-int(request.form.get("shares"))#ile akcji ma USER czyli bierzymy jego aktualną ilośc - ile chce sprzedać

        shares_data  =   lookup(request.form.get("symbol"))
        if share == 0:#jeśli sprzedamy wszystkie akcje to usuwamy to z bazy danych portfolio użytkownika
            cash_y=db.execute("SELECT  cash  FROM users WHERE id = ?",session["user_id"])
            cash_d=cash_y[0]["cash"]
            cash_d = cash_d + (int(request.form.get("shares")) * shares_data["price"])
            db.execute("UPDATE users SET cash = ? WHERE id = ?",cash_d,session["user_id"])
            db.execute("DELETE FROM portfolio WHERE symbol = ? AND user_id = ?",request.form.get("symbol"),session["user_id"])
            db.execute("INSERT INTO buy2 (user_id,company,symbol,shares,price,type) VALUES (?,?,?,?,?,?)",session["user_id"],shares_data["name"],shares_data["symbol"],request.form.get("shares"),shares_data["price"],"sell")
            flash("SOLD")


        else:

            db.execute("UPDATE portfolio SET shares = ? WHERE user_id = ? AND symbol = ?",share, session["user_id"],request.form.get("symbol"))#jęsli nie sprzedaje wszystkich akcji to zmieniamy tylko ich ilość
            cash_x=db.execute("SELECT  cash  FROM users WHERE id = ?",session["user_id"])#pobieramy ile pieniędzy ma użytkownik
            cash=cash_x[0]["cash"]

            cash = cash + (share * shares_data["price"])#do aktualnej ilości gotówki dodajemy ilość sprzedanych akcji razy bo tyle zarobił
            db.execute("UPDATE users SET cash = ? WHERE id = ?",cash,session["user_id"])
            db.execute("INSERT INTO buy2 (user_id,company,symbol,shares,price,type) VALUES (?,?,?,?,?,?)",session["user_id"],shares_data["name"],shares_data["symbol"],request.form.get("shares"),shares_data["price"],"sell")

            flash("SOLD-działa okej")

        return redirect("/")





    return render_template("sell.html",symbols=symbols)

@app.route("/change_password", methods=["GET", "POST"])
@login_required
def change_pass():

    if request.method == "POST":
         new_password = request.form.get("new_password")
         new_pass_again = request.form.get("new_pass_again")


         if not new_password or not new_pass_again:
                                                                           #sprawdzam czy wszystkie pola zostały wypełnione:

             return apology("You have to Fill all inputs")

         if str(new_password) != str(new_pass_again):
                                                              #sprawdzam czy hasła się zgadzają
             return apology("Password dosent matches")

         reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
         pat = re.compile(reg)
         match = re.search(pat,new_password)
         if match:
            db.execute("UPDATE users SET hash = ? WHERE id = ?",generate_password_hash(request.form.get("new_password")),session["user_id"])
            flash("you sucessfuly change your password")
            return redirect ("/")
         else:


            flash("you dont achive conditions")
            return render_template("change.html")

    return render_template("change.html")


