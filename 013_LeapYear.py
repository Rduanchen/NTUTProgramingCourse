def judgeYear(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    return False


Iyear = [int(input()) for i in range(2)]

for i in Iyear:
    if judgeYear(i):
        print("Leap Year")
    else:
        print("Common Year")
