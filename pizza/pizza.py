from tabulate import tabulate
import sys
import csv

def main():
    items = []
    plik = check_file()
    try:
        file = open(plik,"r")
    except FileNotFoundError:
        sys.exit("File does not exist")
    dict = csv.DictReader(file)
    for line in dict:
        items.append(line)
    output(items)

def check_file():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:

        if sys.argv[1].find(".csv") != -1:

            return sys.argv[1]

        else:
            sys.exit("Not a CSV file")

def output(items):

    print(tabulate(items,headers = "keys",tablefmt="grid"))

if __name__ == "__main__":
    main()