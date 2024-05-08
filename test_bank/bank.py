def main():

    var = input("Greeting: ")
    print(value(var))


def value(greets):
    greet_lower = greets.lower().replace(","," ").split()
    greet = greet_lower[0]

    if greet[0] =='h' and greet != "hello":
        return "$20"
    elif greet == "hello":
        return "$0"
    else:
        return "$100"


if __name__ == "__main__":

    main()


