import sys
from pyfiglet import Figlet
from random import choice

figlet = Figlet()


def main():

    if len(sys.argv) == 1:

        font = choice(figlet.getFonts())  # get the random font
        var = input("Input: ")
        figlet.setFont(font=font)

    elif len(sys.argv) == 3:

        if sys.argv[1] == "-f" or sys.argv[1] == "--font":

            if sys.argv[2] in figlet.getFonts():
                var = input("Input: ")
                figlet.setFont(font=sys.argv[2])
            else:

                sys.exit("Invalid Usage")
        else:

            sys.exit("Invalid Usage")
    else:

        sys.exit("Invalid Usage")

    print(figlet.renderText(var))


main()
