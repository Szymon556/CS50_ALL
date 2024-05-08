def main():
    money = 50
    while True:
        coin = int(input("Insert Coin: "))
        if coin==25 or coin==10 or coin==5 or coin == 50:
            money = money - coin
            if money>=0:
                print("Amount due:",money)

                if money == 0:
                    break

            else:
                print("Change owed:", money*(-1))
                break



        else:
            if money>=0:

                print("Amount due: ",money)
                if money == 0:
                    break

            else:
                print("Change owed:", money*(-1))
                break






main()