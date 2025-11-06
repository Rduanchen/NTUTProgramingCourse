courseList = [
    {"number": int(input()), "times": [int(input()), int(input())]} for _ in range(3)
]

# 按課程編號排序
for i in range(3):
    for x in range(i + 1, 3):
        if courseList[i]["number"] < courseList[x]["number"]:
            courseList[i], courseList[x] = courseList[x], courseList[i]

conflicts = []

# print(courseList) # for debug

# 所有課程兩兩比較
for i in range(3):
    for j in range(i + 1, 3):
        course1 = courseList[i]
        course2 = courseList[j]
        # 找出交集時間並排序
        for time in sorted(set(course1["times"]) & set(course2["times"])):
            conflicts.append((course1["number"], course2["number"], time))

# 輸出結果
if conflicts:
    for c in conflicts:
        print(f"{c[0]} and {c[1]} conflict on {c[2]}")
else:
    print("correct")
