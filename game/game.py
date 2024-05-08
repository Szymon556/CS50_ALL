import random
import sys
def guess(x):

    while True:

        try:
            gs = int(input("Guess: "))
        except ValueError:
            pass
        else:

            if 0<gs:
                if gs<x:
                    print("Too small!")
                elif gs>x:
                    print("Too large!")
                else:
                    print("Just right!")
                    sys.exit()



def main():

    while True:

        try:

            lvl = int(input("Level: "))

        except ValueError:
            pass
        else:
            if lvl>0:
                break
    rand = random.randint(1,lvl)
    guess(rand)


main()