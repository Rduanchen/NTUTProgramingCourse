def scoring(s):
    score = 0
    try:
        s = int(s)
        return 2
    except ValueError:
        if s.islower():
            return 1
        elif s.isupper():
            return 3
        elif s in set("~!@#$%^&*<>_+="):
            return 4.5
        else:
            return 0


def isDigitalContinues(password):
    digit_positions = [i for i, c in enumerate(password) if c.isdigit()]
    if len(digit_positions) >= 5:
        for i in range(len(digit_positions) - 1):
            if digit_positions[i] + 1 == digit_positions[i + 1]:
                return 0
        return 10
    return 0


amount = int(input())
passwords = []

for i in range(amount):
    password = input()
    score = 0
    for x in password:
        score += scoring(x)

    score += isDigitalContinues(password)

    if len(password) > 8:
        score += len(password) - 8

    if "1234" in password:
        score -= 10

    passwords.append((password, score))

passwords.sort(key=lambda x: x[1])
print(f"{passwords[-1][0]} {passwords[-1][1]:.1f}")
print(f"{passwords[0][0]} {passwords[0][1]:.1f}")
