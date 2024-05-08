def main():

    word = input("Enter a value: ")

    print(shorten(word))


def shorten(word):

        
    vovels = ["a","e","i","o","u","A","E","I","O","U"]
    result = []
    i = 0
    for a in word:
        if a in vovels:

            word = word.replace(a,"")

    return word
if __name__ == "__main__":
    main()