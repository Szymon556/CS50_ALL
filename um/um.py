import re

def main():
    print(count(input("Text: ")))

def count(s):

    pattern = re.findall(r"\bum\b",s, re.IGNORECASE)

    if pattern:

        return len(pattern)
    else:

        return 0

if __name__ == "__main__":
    main()