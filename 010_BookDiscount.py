import math

inputA = [int(i) for i in input().split()]
bookA = [380, inputA[0], 1, inputA[1], inputA[2], inputA[3]]
inputB = [int(i) for i in input().split()]
bookB = [1200, inputB[0], 1, inputB[1], inputB[2], inputB[3]]
inputC = [int(i) for i in input().split()]
bookC = [180, inputC[0], 1, inputC[1], inputC[2], inputC[3]]


def choseTheDiscount(amount, arr):
    if amount >= 31:
        return arr[5] / 100
    elif amount >= 21:
        return arr[4] / 100
    elif amount >= 11:
        return arr[3] / 100
    else:
        return arr[2]


def countThePrice(bookarr):
    amount = bookarr[1]
    discount = choseTheDiscount(amount, bookarr)
    total = math.ceil(bookarr[0] * amount * discount)
    return total


def matchBookName(index):
    match index:
        case 0:
            return "A"
        case 1:
            return "B"
        case 2:
            return "C"


def main():
    priceList = [countThePrice(bookA), countThePrice(bookB), countThePrice(bookC)]
    totalPrice = sum(priceList)
    max = priceList[0]
    min = priceList[0]
    maxIndex = 0
    minIndex = 0
    for i in range(len(priceList)):
        if priceList[i] > max:
            max = priceList[i]
            maxIndex = i
        if priceList[i] < min:
            min = priceList[i]
            minIndex = i

    # output
    print("{}: {}".format(matchBookName(maxIndex), max))
    print("{}: {}".format(matchBookName(minIndex), min))
    print(totalPrice)


main()
