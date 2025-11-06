def original(row, col, level):
    return (row - 1) * level + col


def transform(row, col, op, level):
    match op:
        case "R":
            return col, level - row + 1
        case "L":
            return level - col + 1, row
        case "V":
            return level - row + 1, col
        case "H":
            return row, level - col + 1
    return row, col


def getOriginalIndex(row, col, ops, level):
    for op in reversed(ops):
        match op:
            case "R":
                row, col = transform(row, col, "L", level)
            case "L":
                row, col = transform(row, col, "R", level)
            case "V":
                row, col = transform(row, col, "V", level)
            case "H":
                row, col = transform(row, col, "H", level)
    return row, col


def main():
    level = int(input())
    ops = input().strip()
    print(ops)
    row = col = 1
    for index in range(1, level * level + 1):
        o_row, o_col = getOriginalIndex(row, col, ops, level)
        print(original(o_row, o_col, level), end=" ")
        if col % level == 0:
            col = 0
            row += 1
            print()
        col += 1


main()
