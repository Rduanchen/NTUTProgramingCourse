priceTable = [
    [380, 1, 0.9, 0.85, 0.8],
    [1200, 1, 0.95, 0.85, 0.8],
    [180, 1, 0.85, 0.8, 0.7],
]


def decided_discount(amount):
    if amount >= 31:
        return 4
    elif amount >= 21:
        return 3
    elif amount >= 11:
        return 2
    elif amount >= 1:
        return 1
    else:
        return None


def count_price(book, amount):
    match book:
        case "A":
            price = priceTable[0][0]
            discount = priceTable[0][decided_discount(amount)]
            total = price * amount * discount
        case "B":
            price = priceTable[1][0]
            discount = priceTable[1][decided_discount(amount)]
            total = price * amount * discount
        case "C":
            price = priceTable[2][0]
            discount = priceTable[2][decided_discount(amount)]
            total = price * amount * discount
        case _:
            return None
    return total


bookAamount = int(input())
bookBamount = int(input())
bookCamount = int(input())

boolA = count_price("A", bookAamount)
boolB = count_price("B", bookBamount)
boolC = count_price("C", bookCamount)
sum = int(boolA + boolB + boolC)
print(sum)
