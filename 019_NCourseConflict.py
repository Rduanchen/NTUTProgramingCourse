coursesTime = set()
courseTable = []
isWrong = False


def isAvalidateTime(compare):
    date, time = compare
    date = int(date)
    global isWrong
    if date > 5 or date < 1:
        isWrong = True
    if time not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c"):
        isWrong = True
    return


def courseInput():
    className = input()
    classAmount = int(input())
    courseList = [className]
    for i in range(classAmount):
        time = input()
        isAvalidateTime(time)
        courseList.append(time)
    courseTable.append(courseList)


courseAmount = int(input())
for i in range(courseAmount):
    courseInput()

if isWrong:
    print(-1)
    quit()

conflict = False
for i in range(len(courseTable) - 1):
    for x in range(1, len(courseTable[i])):
        date = courseTable[i][x]
        for y in range(i + 1, len(courseTable)):
            # print("---%d" % (y))
            for z in range(1, len(courseTable[y])):
                # print("--%d" % (z))
                if date == courseTable[y][z]:
                    print("{},{},{}".format(courseTable[i][0], courseTable[y][0], date))
                    conflict = True

print("correct") if conflict == False else conflict == True
