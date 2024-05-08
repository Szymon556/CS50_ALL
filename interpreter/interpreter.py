def calculator(operation):
    x,y,z = operation.split(" ")
    xn = float(x)
    zn = float(z)
    match y:
        case "+":
            return round(xn + zn, 1)
        case "-":
            return round(xn - zn, 1)
        case "/":
            if zn==0:
                return "invalid operation"
            else:
                return round(xn / zn, 1)
        case "*":
            return round(xn * zn, 1)
        case _:
            return "we dont handle this"


input = input("Expression: ")
print(calculator(input))