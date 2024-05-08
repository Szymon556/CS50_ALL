import re
import sys

def main():

    print(validate(input("Ipv4 Address: ")))

def validate(IP):

    match = re.search("^((25[0-5]|2[0-5][0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-5][0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$",IP)

    if match:
        return True
    else:

        return False


if __name__ == "__main__":

    main()