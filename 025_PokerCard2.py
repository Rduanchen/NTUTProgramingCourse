NUMBER_KEY = "number"
COLOR_KEY = "color"

VALID_NUMBERS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
VALID_COLORS = ["S", "H", "D", "C"]


def isCardValid(cards):
    error_input = False
    duplicate_deal = False
    card_set = set()
    for card in cards:
        # 牌長度判斷
        if len(card) < 2 or len(card) > 3:
            error_input = True
            continue
        cardNumber = card[:-1]
        cardColor = card[-1]
        if cardNumber not in VALID_NUMBERS or cardColor not in VALID_COLORS:
            error_input = True
        elif card in card_set:
            duplicate_deal = True
        else:
            card_set.add(card)
    if error_input:
        print("Error input")
        exit()
    elif duplicate_deal:
        print("Duplicate deal")
        exit()
    elif len(cards) != 5:
        print("Error input")
        exit()


def reorganizeCards(cards):
    cardSet = []
    isCardValid(cards)
    for card in cards:
        cardNumber = card[0:-1]
        cardColor = card[-1]

        number = None
        match cardNumber:
            case "A":
                number = 1
            case "J":
                number = 11
            case "Q":
                number = 12
            case "K":
                number = 13
            case "10":
                number = 10
            case _:
                number = int(cardNumber)
        cardSet.append({"number": number, "color": cardColor})
    cardSet = sorted(cardSet, key=lambda x: x["number"])
    return cardSet


def isSameNumber(cards, amount):
    cardNumberSets = [card[NUMBER_KEY] for card in cards]
    for toFIndCard in cards:
        if cardNumberSets.count(toFIndCard[NUMBER_KEY]) >= amount:
            return True
    return False


def isSameColor(cards):
    if [card[COLOR_KEY] for card in cards].count(cards[0][COLOR_KEY]) == 5:
        return True
    return False


def isAPair(cards):
    cardNumberSets = [card[NUMBER_KEY] for card in cards]
    for toFIndCard in cards:
        if cardNumberSets.count(toFIndCard[NUMBER_KEY]) >= 2:
            return True
    return False


def isTwoPair(cards):
    cardNumberSets = [card[NUMBER_KEY] for card in cards]
    pair = 0
    for i in range(2):
        for card in cardNumberSets:
            if cardNumberSets.count(card) >= 2:
                cardNumberSets.remove(card)
                cardNumberSets.remove(card)
                pair += 1
                break
    return True if pair == 2 else False


def isNumberContinue(cards, countinueAmout):
    cardNumberSets = [card[NUMBER_KEY] for card in cards]
    cardNumberSets.extend([(i + 13) for i in cardNumberSets])
    for i in range(6):
        isSameGap1 = True
        comparingSet = cardNumberSets[i : i + countinueAmout]
        for index in range(len(comparingSet) - 1):
            if abs(comparingSet[index] - comparingSet[index + 1]) != 1:
                isSameGap1 = False
                break
        if isSameGap1:
            return True
    return False


def isFullHouse(cards):
    amount = 3
    cardNumberSets = [card[NUMBER_KEY] for card in cards]
    for toFIndCard in cards:
        if cardNumberSets.count(toFIndCard[NUMBER_KEY]) >= amount:
            cardNumberSets.remove(toFIndCard[NUMBER_KEY])
            cardNumberSets.remove(toFIndCard[NUMBER_KEY])
            cardNumberSets.remove(toFIndCard[NUMBER_KEY])
            break

    if len(cardNumberSets) > 2:
        return False
    else:
        if cardNumberSets[0] == cardNumberSets[1]:
            return True
        else:
            return False


def main():
    pokerCards = reorganizeCards(input().split())
    # print(isNumberContinue(pokerCards, 5))
    conditions = [False for i in range(0, 11)]
    conditions[1] = True
    conditions[2] = isAPair(pokerCards)
    conditions[3] = isTwoPair(pokerCards)
    conditions[4] = isSameNumber(pokerCards, 3)
    conditions[5] = isNumberContinue(pokerCards, 5)
    conditions[6] = isSameColor(pokerCards)
    conditions[7] = isFullHouse(pokerCards)
    conditions[8] = isSameNumber(pokerCards, 4)
    conditions[9] = isNumberContinue(pokerCards, 5) and isSameColor(pokerCards)
    for i in range(9, 0, -1):
        if conditions[i] == True:
            print(i)
            break


main()
