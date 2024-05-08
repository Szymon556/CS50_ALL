import inflect

p = inflect.engine()


def main():
    list = []
    while True:

        try:

            var = input("Name: ")
            list.append(var)

        except EOFError:

            break
    output = p.join(list)
    print("Adieu, adieu, to " + output)


main()
