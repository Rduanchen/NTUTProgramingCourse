def decidedPokerPoint(num):
    if num == "A":
        return 1
    elif num == "J" or num == "Q" or num == "K":
        return 0.5
    else:
        return int(num)


def countSum(cards):
    total = 0
    for card in cards:
        total += decidedPokerPoint(card)
    if total > 10.5:
        return 0
    return total


def decideWhoWin(a, b):
    sumA = countSum(a)
    sumB = countSum(b)
    print(int(sumA) if sumA == int(sumA) else sumA)
    print(int(sumB) if sumB == int(sumB) else sumB)
    if 10.5 - sumA < 10.5 - sumB:
        print("X Win")
    elif 10.5 - sumA > 10.5 - sumB:
        print("Y Win")
    else:
        print("Tie")


playerA = [input() for i in range(3)]
playerB = [input() for i in range(3)]
decideWhoWin(playerA, playerB)
