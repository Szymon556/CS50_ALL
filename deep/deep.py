x = input("What is the answer to the Great Question of Life, the Universe and Everything: ")
x_lower = x.lower().strip()
match x_lower:
    case "42"|"forty-two"|"forty two":
        print("Yes")
    case _:
        print("No")
