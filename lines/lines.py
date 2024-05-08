import sys



def main():
    counter = 0
    plik = sprawdzenie()
    try:
        with open(plik,"r") as file:
            for line in file:
                if not line.isspace():
                     #czyli w przypadku gdy linia nie składa się z samych spacji
                    line = line.strip()#usuwamy spacje
                    if not line[0] == '#':#sprawdzamy czy to nie jest linia która zawiera tylko komentarz
                        counter += 1


    except FileNotFoundError:
        sys.exit("File does not exist")
    print(counter)

def sprawdzenie():

    if len(sys.argv) < 2:

        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    else:
        if not sys.argv[1].find(".py") == -1:

            return sys.argv[1]
        else:
            sys.exit("Not a python file")


if __name__ == "__main__":
    main()