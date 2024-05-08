def main():
    name = input("camelCase: ")
    snake_case(name)

def snake_case(nameCamel):

    for c in nameCamel:

        if c.isupper():
            x=c.lower()
            c="_"
            print(c+x, end="")
        else:
            print(c, end="")
    print()

main()