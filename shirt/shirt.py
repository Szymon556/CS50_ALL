from PIL import Image,ImageOps
import sys

def main():
    check_input()#sprawdzay czy użytkownik podał odpowiednie dane w kosnoli
    try:
        muppet = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")

    size = shirt.size #pobieramy wielkość koszulki żeby do niej dopasować obrazy
    muppet = ImageOps.fit(muppet,size)
    muppet.paste(shirt, shirt)
    muppet.save(sys.argv[2])

    


def check_input():
    extension = ["png","jpg","jpeg"]
    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    else:
        name = sys.argv[1].split(".")#podzielimy nazwy i rozszerzenia zeby potem porówanć oraz sprawdzić rozszwerzenia
        name2 = sys.argv[2].split(".")

        if name[1] in extension and name2[1] in extension:

            if name[1] == name2[1]:

                return
            else:

                sys.exit("Input and output have different extensions")
        else:

            sys.exit("Invalid output")




if __name__ == "__main__":

    main()