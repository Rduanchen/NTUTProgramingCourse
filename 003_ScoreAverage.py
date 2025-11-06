Name = input()
ID = input()
ChineseScore = int(input())
ComputerScore = int(input())
ProgrammingScore = int(input())

TotalScore = ChineseScore + ComputerScore + ProgrammingScore
AverageScore = int((ChineseScore + ComputerScore + ProgrammingScore) / 3)

print("Name:{}".format(Name))
print("Id:{}".format(ID))
print("Total:{}".format(TotalScore))
print("Average:{}".format(AverageScore))
