import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r'src *= *"(https?://(www\.)?youtube\.com/embed/(\w+))"', s, re.IGNORECASE)
    if match:
        replaced_url = re.sub(
            r"^(http(s)?://)?(www\.)?youtube\.com/embed/",
            "https://youtu.be/",
            match.group(1),
        )

        return replaced_url
    else:
        return None


if __name__ == "__main__":

    main()
