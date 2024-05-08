import re

def main():
    print(convert(input("Hours: ").strip()))

def convert(s):

    match = re.search(r"([1-9]|1[0-2])(?::([0-5][0-9]))? ([AP]M) *to *([1-9]|1[0-2])(?::([0-5][0-9]))? ([AP]M)",s)
    if match:
        list = match.groups()
        first_time = format(list[0],list[1],list[2])
        second_time = format(list[3],list[4],list[5])
        return f"{first_time} to {second_time}"
    else:
        raise ValueError








def format(hour,minute,am_pm):

    if am_pm == "PM":
        if int(hour)>12:
            raise ValueError
        if int(hour) == 12:
            new_h = 12
        else:
            new_h = int(hour) + 12
    elif am_pm == "AM":
        if int(hour)>12:
            raise ValueError
        if int(hour) == 12:
            new_h = 00
        else:
            new_h = hour
    if minute == None:

        if len(str(new_h)) == 1:# w przypadku gdy mamy np 9 AM żeby wpisało 09:00

            return f"0{new_h}:00"
        else:# w przypadku gdy mamy np 6 PM żeby wpisało 18:00
            return f"{new_h}:00"
    elif minute != None:

        if len(str(new_h)) == 1:

            return f"0{new_h}:{minute}"
        else:

            return f"{new_h}:{minute}"









if __name__ == "__main__":
    main()