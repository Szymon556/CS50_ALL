


def main():

    x = int(round(get_float("Fraction: "),2)*100)


    if x >= 99:
        print("F")
    elif x <=1:
        print("E")
    else:
        print(str(x)+"%")


def get_float(prompt):

    while True:
        try:
           value = input(prompt).split('/')

           if int(value[0])<=int(value[1]):

                return  int(value[0])/int(value[1])

        except ValueError:
            pass
        except ZeroDivisionError:
            pass
main()