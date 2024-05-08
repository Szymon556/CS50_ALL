# TODO
from cs50 import get_string


def main():

    input = get_string("Enter text: ").lower()

    words = input.count(" ") + 1

    letters = 0

    sentences = input.count(".")+input.count("?")+input.count("!")

    for x in input:

        if x.isalpha():
            letters = letters + 1

    L = (letters/words)*100
    print(L)
    S = (sentences/words)*100
    print(S)

    index = round(0.0588 * L - 0.296 * S - 15.8)

    if index < 1:
        print("Before Grade 1")
    elif index > 15:
        print("Grade 16+")
    else:
        print(f"Grade {index}")


main()