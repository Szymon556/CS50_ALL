import re

def check_greetings(greets):
    greet_lower = greets.lower().replace(","," ").split()
    greet = greet_lower[0]
    print(greet)
    if greet[0] =='h' and greet != "hello":
        print("$20")
    elif greet == "hello":
        print("$0")
    else:
        print("$100")

def main():
    x = input("Greeting: ")
    check_greetings(x)

main()