amount = 3
lineList = [[int(input()), int(input())] for _ in range(amount)]
# sort
for i in range(amount):
    for x in range(i + 1, amount):
        if lineList[i][0] > lineList[x][0]:
            lineList[i], lineList[x] = lineList[x], lineList[i]

newList = [[lineList[0][0], lineList[0][1]]]
for i in lineList[1:]:
    last = newList[-1]
    if i[0] <= last[1]:
        last[1] = max(last[1], i[1])
    else:
        newList.append([i[0], i[1]])
total = sum(abs(i[1] - i[0]) for i in newList)

print(total)
