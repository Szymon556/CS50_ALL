# TODO
from cs50 import get_float




def main():

    while True:

         input = get_float("Enter the value: ")

         check_float = isinstance(input,float)


         if input > 0 and check_float:
            break


    counter = calculate_quarters(input)
    input = round(input-(0.25*counter), 3)

    counter = counter+calculate_dimes(input)
    input = round(input-(0.1*calculate_dimes(input)), 3)


    counter = counter+calculate_nickles(input)
    input = round(input-(0.05*calculate_nickles(input)),3)

    counter = counter+calculate_pennies(input)


    print(counter)



def calculate_quarters(input):

    x = 0

    while True:


        if input >= 0.25:
            input = input - 0.25
            x = x+1
        else:
            break


return x


def calculate_dimes(input):

    x = 0

    while True:

        if input >= 0.1:
            input = input - 0.1
            x = x + 1

        else:
            break


return x


def calculate_nickles(input):

    x = 0

    while True:

        if input >= 0.05:
            input = input - 0.05
            x = x + 1
        else:
            break

    return x


def calculate_pennies(input):

    x = 0

    while True:

        if input >= 0.01:
            input = input - 0.01
            x = x + 1
        else:
            break

    return x


main()