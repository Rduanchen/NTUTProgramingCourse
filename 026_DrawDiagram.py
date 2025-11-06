def drawDiagram(amount, symbol):
    print(symbol * amount, end="")


def leftDiagram(rowId, height):
    drawDiagram(rowId, "*")


def middleDiagram(rowId, height):
    symbolAmount = (height - rowId) * 2
    drawDiagram(symbolAmount, "_")


def rightTriangle(rowID, height):
    symbolAmount = (rowID - 1) * 2 + 1
    drawDiagram(symbolAmount, "*")


def rightDash(rowID, height):
    symbolAmount = height - rowID
    drawDiagram(symbolAmount, "_")


def drawFish(height, pointDir):
    if (pointDir + 2) % 2 == 0:
        for row in range(1, height + 1):
            leftDiagram(row, height)
            middleDiagram(row, height)
            rightTriangle(row, height)
            rightDash(row, height)
            print()
        for row in range(height - 1, 0, -1):
            leftDiagram(row, height)
            middleDiagram(row, height)
            rightTriangle(row, height)
            rightDash(row, height)
            print()
    else:
        for row in range(1, height + 1):
            rightDash(row, height)
            rightTriangle(row, height)
            middleDiagram(row, height)
            leftDiagram(row, height)
            print()
        for row in range(height - 1, 0, -1):
            rightDash(row, height)
            rightTriangle(row, height)
            middleDiagram(row, height)
            leftDiagram(row, height)
            print()


def drawDash2(rowID, height):
    drawDiagram(height - rowID, "_")


def drawTriangle2(rowID, height):
    if rowID == 1:
        drawDiagram(1, "1")
    else:
        for i in range(rowID, 0, -1):
            print(i, end="")
        for i in range(2, rowID + 1, 1):
            print(i, end="")


def drawType2(height, pointDir):
    if (pointDir + 2) % 2 == 0:
        for row in range(height, 0, -1):
            drawDash2(row, height)
            drawTriangle2(row, height)
            drawDash2(row, height)
            print()
    else:
        for row in range(1, height + 1, 1):
            drawDash2(row, height)
            drawTriangle2(row, height)
            drawDash2(row, height)
            print()


def main():
    height = int(input())
    pointDirection = int(input())
    type = int(input())
    if type == 1:
        drawFish(height, pointDirection)
    elif type == 2:
        drawType2(height, pointDirection)


main()
