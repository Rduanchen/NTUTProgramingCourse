color = input().split()
cards = input().split()


def convert2Point(card):
    match (card):
        case "A":
            return 4
        case "K":
            return 3
        case "Q":
            return 2
        case "J":
            return 1
        case _:
            return 0


def suggestion(points):
    if points >= 15:
        return "Strong Open"
    elif points <= 14 and points >= 8:
        return "Open {}".format(longestColor())
    elif points <= 8:
        return "Pass"


def extraPoints():
    for i in howManyCards:
        if howManyCards[i] == 5:
            return 2
    return 0


def countStopSuit():
    stopList = []
    for i in stopSuit:
        if stopSuit[i] >= 4:
            stopList.append(i)
    return stopList


def longestColor():
    longcolor = "S"
    longPoint = howManyCards["S"]
    for i in howManyCards:
        if howManyCards[i] > longPoint:
            longPoint = howManyCards[i]
            longcolor = i
    match (longcolor):
        case "S":
            return "Spade"
        case "H":
            return "Heart"
        case "D":
            return "Diamond"
        case "C":
            return "Club"
        case _:
            return ""


stopSuit = {"S": 0, "H": 0, "D": 0, "C": 0}
howManyCards = {"S": 0, "H": 0, "D": 0, "C": 0}


HCP = 0
for i in range(len(cards)):
    point = convert2Point(cards[i])
    HCP += point
    stopSuit[color[i]] += point
    howManyCards[color[i]] += 1

print("HCP: {}".format(HCP))
total = HCP + extraPoints()
print("Total Points: {}".format(total))
print("Distribution (S-H-D-C): {}-{}-{}-{}".format(*[i for i in howManyCards.values()]))
print("Stopped Suits: {}".format(countStopSuit()))
print("Opening Bid: {}".format(suggestion(total)))
