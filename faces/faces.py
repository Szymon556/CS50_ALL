def convert(value):
    output=value.replace(":)","🙂")
    output=output.replace(":(","🙁")
    return output
def main():
    value = input("Enter:")
    print(convert(value))
main()