def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if s[0:2].isalpha():#sprawdzamy czy dwa pierwsze wyrazy to liter
        if 2<=len(s)<=6:#sprawdzamy czy rozmiar miesci sie miedzy 2 a 6 znakow
            i = 0
            for a in s:

                if a.isdigit():#od pierwszej cyfry
                    if int(a) == 0:
                        return False
                    elif not s[i::].isdigit():#sprawdzamy czy wszystkie nastepne to tez cyfry jesli nie zwroc false
                        return False
                    else:
                        break
                elif not a.isalpha():
                    return False


                i+=1
            return True



        else:
            return False
    else:
        return False



if __name__ == "__main__":
    main()