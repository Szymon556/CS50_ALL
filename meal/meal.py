import re

def main():
    time_i = input("Enter a time: ")
    Ctime = convert(time_i)
    if 7.00<=Ctime <= 8.00:
         print("breakfast time")
    elif 12.00<=Ctime <= 13.00:
        print("lunch time")
    elif 18.00<= Ctime<= 19.00:

        print("dinner time")

def convert(time):
    hours, minuts = re.split(r"[:, ]", time)

    Cminuts = (int(minuts)/60) #konwertujemy minuty
    Chours = int(hours)
    Ctime = Chours+Cminuts
    return Ctime




if __name__ == "__main__":
    main()