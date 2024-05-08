# TODO
from cs50 import get_string
import sys


def lun_alg(input):
    x = 0

    number = int(input)
    checksum=0
    score = []

    while number > 0:
        checksum = checksum + number%10
        number = int(number / 10)#usuwamy ostatnią liczbę
        buffor = (number % 10)*2 #zapisujemy liczbę po niej w liście


        if buffor >= 10: #jeśli liczba jest dwuczłonowa
            score.insert(x+1, buffor % 10)  #to ostatni człon zapisujemy w następnej komórce
            score.insert(x,int(buffor / 10)) #pierwszy człon dajemy w pierwszej komórce(tej oryginalnej gdzie była na początku)
            x = x + 2 #wtedy przedakujemy o dwa indeksy
        else:
            score.insert(x,buffor)
            x = x + 1


        number = int(number / 10)

    return(checksum + sum(score))




def main():

    input=get_string("Enter the number: ")

    if len(input) not in range(13,56):
        print("INVALID")
        sys.exit(0)

    answer=lun_alg(input)




    value=int(input[0]+input[1])



    if value == 40 or int(value/10) == 4 and answer % 10 == 0 and len(input) in range(13,17):
        print("VISA")
    elif value in range(51,56) and answer % 10 == 0 and len(input) == 16:
        print("MASTERCARD")
    elif value == 34 or value == 37 and answer % 10 ==0 and len(input)==15:
        print("AMEX")
    else:
        print("INVALID")


main()






