import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Add the user's entry into the database

            name=request.form.get("name")
            month=request.form.get("month")
            day=request.form.get("day")

            if not name or not month or not day:
                rendert_template("index.html")
            db.execute("INSERT INTO birthdays (name,month,day) VALUES(?,?,?)", name,month,day)
            return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html
        birthdays=db.execute("SELECT * FROM birthdays")#pobieramy wszystko z bazy danych i zapisujemy w słowniku
        return render_template("index.html", birthdays=birthdays)


@app.route("/Delete", methods=["POST","GET"])
def delete():

    id = request.form.get("id")
    if id:#sprawdzamy czy dostaliśmy id
        db.execute("DELETE FROM birthdays WHERE id = ?",id)

    return redirect("/")
#@app.route("/Change", methods = ["POST"]) kiedyś do tego wrócę
#def change():

