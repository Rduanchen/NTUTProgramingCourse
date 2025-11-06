def transferPoker2Point(card):
    if card in ("J", "Q", "K"):
        return 0.5
    elif card == "A":
        return 1
    else:
        return int(card)


class Player:
    def __init__(self, stake):
        self.money = 0
        self.pokerPointAmount = 0
        self.stake = stake

    def isBursted(self):
        if self.pokerPointAmount > 10.5:
            return True
        else:
            return False

    def getACard(self, card):
        self.pokerPointAmount += transferPoker2Point(card)
        return self.isBursted()

    def getCurrentPoint(self):
        return self.pokerPointAmount

    def is10point5(self):
        return self.pokerPointAmount == 10.5


class Computer:
    def __init__(self):
        self.money = 0
        self.pokerPointAmount = 0

    def isBursted(self):
        if self.pokerPointAmount > 10.5:
            return True
        else:
            return False

    def getACard(self, card):
        self.pokerPointAmount += transferPoker2Point(card)
        return self.isBursted()

    def isContinue(self, points):
        if len(points) == 0:
            return False
        if self.pokerPointAmount >= 10.5:
            return False
        elif self.pokerPointAmount <= min(points):
            return True
        else:
            return False

    def getCurrentPoint(self):
        return self.pokerPointAmount

    def countPrize(self, players):
        for player in players:
            if player.isBursted():  # 玩家爆掉
                player.money = -player.stake
                self.money += player.stake
                continue

            if player.is10point5() or self.isBursted():  # 玩家10.5點或莊家爆掉
                player.money = player.stake
                self.money -= player.stake
                continue

            # 一般比較：莊家大於等於玩家則莊家勝（玩家輸）
            if player.getCurrentPoint() > self.pokerPointAmount + 1e-9:
                player.money = player.stake
                self.money -= player.stake
            else:
                player.money = -player.stake
                self.money += player.stake

    def getCards(self, players):
        points = []
        for player in players:
            if not (player.isBursted() or player.is10point5()):
                points.append(player.getCurrentPoint())
        while True:
            if self.isContinue(points):
                self.getACard(input())
            else:
                break


def main():
    playerAmount = int(input())
    players = []
    # get stakes
    for stake in input().split():
        players.append(Player(int(stake)))

    # First Round
    firstRoundCard = input().split()
    computer = Computer()
    computer.getACard(firstRoundCard[0])
    for playerID in range(playerAmount):
        players[playerID].getACard(firstRoundCard[playerID + 1])

    # All Player get cards
    for playerID in range(playerAmount):
        while True:
            cardCommand = input().split()

            if cardCommand[0] == "N":
                keepon = False
                break
            else:
                players[playerID].getACard(cardCommand[1])
                if players[playerID].isBursted() or players[playerID].is10point5():
                    break

    # Computer get Card
    computer.getCards(players)
    computer.countPrize(players)

    # Print result
    for i in range(playerAmount):
        printString = (
            "+{}".format(players[i].money) if players[i].money > 0 else players[i].money
        )
        print("Player{} {}".format(i + 1, printString))
    printString = "+{}".format(computer.money) if computer.money > 0 else computer.money
    print("Computer {}".format(printString))


main()
