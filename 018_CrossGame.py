whoFirst = int(input())
steps = [int(i) for i in input().split()]
board = [0 for i in range(9)]
playerSteps = []
computerSteps = []

whosesturn = whoFirst
for i in steps:
    if whosesturn == 1:
        board[i - 1] = whosesturn
        whosesturn = 2
        playerSteps.append(i)
    elif whosesturn == 2:
        board[i - 1] = whosesturn
        whosesturn = 1
        computerSteps.append(i)

for i in range(1, len(board) + 1):
    print(board[i - 1], end=" ")
    if i % 3 == 0:
        print("")


computerSteps = "".join(str(x) for x in sorted(computerSteps))
playerSteps = "".join(str(x) for x in sorted(playerSteps))


def winpatten(patten):
    if patten == "123" or patten == "456" or patten == "789":
        return True
    elif patten == "147" or patten == "258" or patten == "369":
        return True
    elif patten == "159" or patten == "357":
        return True
    else:
        return False


if whoFirst == 1:  # Player First
    if winpatten(playerSteps):
        print("Player win")
    else:
        print("Undecided")
else:
    if winpatten(computerSteps):
        print("Computer win")
    else:
        print("Undecided")


# def sortList(slist):
#     l = slist
#     for i in range(len(l)):
#         for x in range(i + 1, len(l)):
#             if l[i] < l[x]:
#                 l[i], l[x] = l[x], l[i]
#     return l


# def findSecond(slist):
#     max = slist[0]
#     for i in slist:
#         if i != max:
#             return i
#     return max


# final = sortList([int(i) for i in input().split()])
# print(findSecond(final))
