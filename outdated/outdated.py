def main():

    while True:

        x = input("Date: ")


        if sprawdzenie(x):

            break


def sprawdzenie(val):
    dict= {
    "January" : 1,
    "February" : 2,
    "March" : 3,
    "April" : 4,
    "May" : 5,
    "June" : 6,
    "July" : 7,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" : 11,
    "December" : 12,
    }
    if val[0].isdigit():

        val = val.split("/")
        try:
            val0 = int(val[0])
            val1 = int(val[1])
            val2 = int(val[2])
        except ValueError:
            return False
        if 13>int(val0)>0:
            if 32>int(val1)>0:
                print(f"{val2}-{val0:02}-{val1:02}")
                return True
            else:

                return False
        else:

            return False

    elif val[0].isalpha():
        if val.find(",") != -1:

            val = val.replace(",","")
        else:
            return False

        val = val.split(" ")
        if val[0].title() in dict:

            if 32>int(val[1])>0:
                print(f"{val[2]}-{dict[val[0]]:02}-{int(val[1]):02}")
                return True
            else:

                return False
        else:
            return False
    else:

        return False

main()