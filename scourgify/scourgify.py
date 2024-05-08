import sys
import csv

def main():
    file = check_file()
    list_dict = []
    output = []
    try:
        with open(file,"r") as f:
            lines = csv.DictReader(f)#zapisujemy plik jako słownik
            for line in lines: #dla każdego wiersz który jest słownikien
                list_dict.append(line) # dodajemy do listy przez co mamy listę słowników
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
    for line in list_dict: #odczytujemy liestę słowników żeby rodzielić imię i nazwisko na dwie kolumny i zapisac ponownie
       last,first = line["name"].split(",")
       house = line["house"]
       output.append({"first":first.lstrip(),"last":last,"house":house})

    with open(sys.argv[2],"w",newline="") as f2:
        writer = csv.DictWriter(f2,fieldnames = ["first","last","house"])
        writer.writeheader()
        writer.writerows(output)




def check_file():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:

        if sys.argv[1].find(".csv") != -1 or sys.argv[2].find(".csv")!= -1:

            return sys.argv[1]

        else:
            sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()