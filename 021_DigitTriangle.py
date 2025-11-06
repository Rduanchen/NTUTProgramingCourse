def typeone(number):
    for i in range(1, number + 1):
        print(oneline(i))


def oneline(number):
    front = ""
    for x in range(1, number):
        front += str(x)
    middle = number
    back = ""
    for y in range(number - 1, 0, -1):
        back += str(y)
    return "{}{}{}".format(front, middle, back)


def typetwo(number):
    for i in range(1, number + 1):
        patch = "".join(["_" for i in range(number - i)])
        middle = oneline(i)
        print("{}{}{}".format(patch, middle, patch))


def typethree(number):
    for i in range(number, 0, -1):
        patch = "".join(["_" for i in range(number - i)])
        middle = oneline(i)
        print("{}{}{}".format(patch, middle, patch))


def main():
    triangleType = int(input())
    number = int(input())
    if number < 3 or number > 50:
        print("Row Error")
        return
    match (triangleType):
        case 1:
            typeone(number)
        case 2:
            typetwo(number)
        case 3:
            typethree(number)


main()
