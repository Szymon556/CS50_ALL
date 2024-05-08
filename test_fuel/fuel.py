def main():

    prompt = input("Fraction: ")
    x = convert(prompt)
    print(gauge(x))


def convert(prompt):
    while True:
        try:
           value = prompt.split('/')

           f = int(value[0])/int(value[1])

           if f<=1:
                result = int(f*100)
                return result
           else:
                prompt = input("Fraction: ")
                pass

        except ValueError:
            raise ValueError("Only Integers")
        except ZeroDivisionError:
            raise ZeroDivisionError("Cant Devide by Zero")


def gauge(x):
    if x >= 99:
        return "F"
    elif x <=1:
        return "E"
    else:
        return str(x)+"%"


if __name__ == "__main__":
    main()