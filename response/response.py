from validator_collection import checkers


def main():
    email = input("Enter a email: ")

    if validation := checkers.is_email(email):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
