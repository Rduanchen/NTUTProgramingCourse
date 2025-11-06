a = int(input())
b = int(input())
c = int(input())


def isATriangle(a: int, b: int, c: int) -> bool:
    if a + b < c:
        return False
    if a + c < b:
        return False
    if b + c < a:
        return False
    return True


def isEquilateralTriangle(a: int, b: int, c: int) -> bool:
    if a == b and b == c:
        return True
    return False


def isIsoscelesTriangle(a: int, b: int, c: int) -> bool:
    if a == b or b == c or c == a:
        return True
    return False


def isObtuseTriangle(a: int, b: int, c: int) -> bool:
    if a**2 > (b**2 + c**2) or b**2 > (a**2 + c**2) or c**2 > (b**2 + a**2):
        return True
    return False


def isAcuteTriangle(a: int, b: int, c: int) -> bool:
    if a**2 < (b**2 + c**2) and b**2 < (a**2 + c**2) and c**2 < (b**2 + a**2):
        return True
    return False


def isRightAngleTriangle(a: int, b: int, c: int) -> bool:
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        return True
    return False


if not isATriangle(a, b, c):
    print("Not Triangle")
else:
    if isEquilateralTriangle(a, b, c):
        print("Equilateral Triangle")
    if isIsoscelesTriangle(a, b, c):
        print("Isosceles Triangle")
    if isObtuseTriangle(a, b, c):
        print("Obtuse Triangle")
    if isAcuteTriangle(a, b, c):
        print("Acute Triangle")
    if isRightAngleTriangle(a, b, c):
        print("Right Triangle")
