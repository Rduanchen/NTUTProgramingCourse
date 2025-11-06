class Player:
    def __init__(self):
        self.pokerCards = []

    def getCards(self):
        self.pokerCards = input().split()
        self.discardSameCard()

    def discardSameCard(self):
        newCardSet = []
        amount = len(self.pokerCards)
        for toSearch in range(amount):
            isSame = False
            for compare in range(amount):
                if toSearch == compare:
                    continue
                if self.pokerCards[toSearch][1] == self.pokerCards[compare][1]:
                    isSame = True
                    break
            if isSame == False:
                newCardSet.append(self.pokerCards[toSearch])
        self.pokerCards = newCardSet

    def cardisTaken(self, takenCards):
        if takenCards in self.pokerCards:
            self.pokerCards.remove(takenCards)
        else:
            print("Error")
            exit()

    def appendCard(self, appendCard):
        self.pokerCards.append(appendCard)
        self.discardSameCard()

    def printPokerCards(self):
        print(" ".join(self.pokerCards))


def main():
    player1, player2, computer = Player(), Player(), Player()
    player1.getCards()
    player2.getCards()
    computer.getCards()
    round1 = input()
    player2.cardisTaken(round1)
    player1.appendCard(round1)
    round2 = input()
    computer.cardisTaken(round2)
    player2.appendCard(round2)
    round3 = input()
    player1.cardisTaken(round3)
    computer.appendCard(round3)
    player1.printPokerCards()
    player2.printPokerCards()
    computer.printPokerCards()


main()
