import inflect
import re
import datetime
import sys

p = inflect.engine()


def main():
    time = validate_time(input("Enter a date: "))
    if time == None:
        sys.exit("Invalid Name")

    birthday = datetime.date(int(time[0]), int(time[1]), int(time[2]))
    today_date = datetime.date.today()
    d = today_date - birthday
    words = p.number_to_words(int(d.days) * (24 * 60), andword="")

    print(words.capitalize() + " minutes")


def validate_time(time):

    match = re.search(
        "^[0-9][0-9][0-9][0-9]-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$", time
    )
    if match:
        return time.split("-")
    else:
        return None


if __name__ == "__main__":
    main()
