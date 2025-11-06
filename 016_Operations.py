operation = input().split()


def do_multiplication(x, y):
    return float(x) * float(y)


def do_division(x, y):
    return float(x) / float(y)


for x in range(2):
    for i in range(len(operation)):
        if operation[i] == "*":
            operation[i] = do_multiplication(operation[i - 1], operation[i + 1])
            operation[i - 1] = "$"
            operation[i + 1] = "$"
            break
        elif operation[i] == "/":
            operation[i] = do_division(operation[i - 1], operation[i + 1])
            operation[i - 1] = "$"
            operation[i + 1] = "$"
            break
    operation = [i for i in operation if i != "$"]

operation = [float(i) if i != "+" and i != "-" else i for i in operation]

hold = 0
final_ans = operation[0]
for i in range(1, len(operation)):
    if operation[i] == "+":
        final_ans = final_ans + operation[i + 1]
    elif operation[i] == "-":
        final_ans = final_ans - operation[i + 1]

print("%.2f" % (final_ans))


# Fast solution:

# expression = input()
# result = eval(expression)
# print(f"{result:.2f}")
