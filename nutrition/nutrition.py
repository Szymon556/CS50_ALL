def main():

    dict = {
        "Apple" : 130,
        "Avocado" : 50,
        "Banana" : 110,
        "Cantaloupe" : 50,
        "Grapefruit" : 60,
        "Grapes" : 90,
        "Honeydew Melon" : 50,
        "Kiwifruit" : 90,
        "Lemon" : 15,
        "Lime" : 20,
        "Nectarince" : 60,
        "Orange" : 80,
        "Peach" : 60,
        "Pear" : 100,
        "Pineapple" : 50,
        "Plums" : 70,
        "Strawberries" : 50,
        "Sweet Cherries" : 100,
        "Tangerine" : 50,
        "Watermelon" : 80
    }

    x = input("Item: ")
    x_con=x.lower().title()

    if x_con in dict:
        print("Calories:",dict[x_con])

main()