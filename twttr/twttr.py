def main():
    vovels = ["a","e","i","o","u","A","E","I","O","U"]
    value = input("Enter a value: ")


    for a in value:
        if not a in vovels:
            print(a, end="")

    print()
main()