SPACE = "__"
FIELD_SIZE = 5


def Ai(row, col, current):
    changeCommands = []
    for rowID in range(FIELD_SIZE):
        if rowID == row:
            continue
        if current[rowID][col] != SPACE:
            changeCommands.append([row, col, "Cn"])
            break
    return changeCommands


def Cn(row, col, current):
    changeCommands = []
    if row != 0 and current[row - 1][col] != SPACE:
        current[row][col] = "Hy"
        changeCommands = [[row, col, "Hy"]]
    return changeCommands


def Hy(row, col, current):
    nearByPlantes = 0
    nearBySpaceIndex = []
    changeCommands = []
    if row != 0:
        if current[row - 1][col] != SPACE:
            nearByPlantes += 1
        else:
            nearBySpaceIndex.append([row - 1, col])
    if row != 4:
        if current[row + 1][col] != SPACE:
            nearByPlantes += 1
        else:
            nearBySpaceIndex.append([row + 1, col])
    if col != 0:
        if current[row][col - 1] != SPACE:
            nearByPlantes += 1
        else:
            nearBySpaceIndex.append([row, col - 1])
    if col != 4:
        if current[row][col + 1] != SPACE:
            nearByPlantes += 1
        else:
            nearBySpaceIndex.append([row, col + 1])
    if nearByPlantes >= 2:
        for field in nearBySpaceIndex:
            changeCommands.append([field[0], field[1], "Na"])
    return changeCommands


def Na(row, col, current):
    changeCommands = []
    if col != 4:
        if current[row][col + 1] == SPACE:
            changeCommands.append([row, col + 1, "Qx"])
    if col != 0:
        changeCommands.append([row, col - 1, "Hy"])
    return changeCommands


def Qx(row, col, current):
    changeCommand = []
    rowField = current[row]
    for colItem in rowField:
        if colItem == SPACE:
            continue
        sameAmount = rowField.count(colItem)
        if sameAmount >= 3:
            for i in range(FIELD_SIZE):  # Find the same Item
                if rowField[i] == colItem:
                    changeCommand.append([row, i, "Ai"])  # modify it
            return changeCommand
    return changeCommand


def modifyTheField(commands, field):
    if not commands:
        return field
    for command in commands:
        field[command[0]][command[1]] = command[2]
    return field


def main():
    totalDays = int(input())
    farm = [input().split() for i in range(FIELD_SIZE)]
    for day in range(totalDays):
        isModifiedThisTurn = [
            [False for _ in range(FIELD_SIZE)] for _ in range(FIELD_SIZE)
        ]
        for row in range(FIELD_SIZE):
            for col in range(FIELD_SIZE):
                if isModifiedThisTurn[row][col]:
                    continue
                commands = []
                if farm[row][col] == "Ai":
                    commands = Ai(row, col, farm)
                elif farm[row][col] == "Cn":
                    commands = Cn(row, col, farm)
                elif farm[row][col] == "Hy":
                    commands = Hy(row, col, farm)
                elif farm[row][col] == "Na":
                    commands = Na(row, col, farm)
                elif farm[row][col] == "Qx":
                    commands = Qx(row, col, farm)
                if commands:
                    for command in commands:
                        targetRow, targetCol, value = command
                        # if farm[targetRow][targetCol] != value:
                        farm[targetRow][targetCol] = value
                        isModifiedThisTurn[targetRow][targetCol] = True

    for row in farm:
        print(" ".join(row))


main()
