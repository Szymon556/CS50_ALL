import random


def main():
    score = 0
    failure = 0
    lvl = get_level()
    for _ in range(10):
        integer1 = generate_integer(lvl)
        integer2 = generate_integer(lvl)
        print(f"{integer1} + {integer2} = ",end="")
        while True:
            try:
                answer = int(input())
            except ValueError:
                failure+=1
                if failure!=3:
                    print("EEE")
                    print(f"{integer1} + {integer2} = ",end="")
                elif failure==3:
                    print(f"{integer1} + {integer2} = ",integer1+integer2)
                    failure=0
                    break
            else:
                if integer1+integer2 == answer:
                    score+=1
                    failure = 0
                    break
                else:
                    failure+=1

                    if failure == 3:
                        failure = 0
                        print(f"{integer1} + {integer2} = ",integer1+integer2)
                        break
                    else:
                        print("EEE")
                        print(f"{integer1} + {integer2} = ",end="")


    print("Score: ",score)

def get_level():
    
    while True:
        try:
            level = int(input("Level: " ))
        except ValueError:
            pass
        else:
            if level == 1 or level == 2 or level == 3:
                return level


def generate_integer(lvl):

    if lvl == 1:
        return random.randint(0,9)
    elif lvl == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)


if __name__ == "__main__":
    main()