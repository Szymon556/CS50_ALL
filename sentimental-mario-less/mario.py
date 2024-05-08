# TODO
from cs50 import get_int


def main():

    height = user_prompt()

    for x in range(height):
        print(" "*(height-(x+1))+"#"*(x+1))


def user_prompt():
    while True:
        x = get_int("Enter the height: ")

        if x > 0 and x < 9:
            break

    return x


main()