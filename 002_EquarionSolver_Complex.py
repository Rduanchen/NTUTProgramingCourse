import math

a = int(input())
b = int(input())
c = int(input())

discriminant = b * b - 4 * a * c
if discriminant >= 0:
    ans1 = ((-b) + math.sqrt(discriminant)) / (2 * a)
    ans2 = ((-b) - math.sqrt(discriminant)) / (2 * a)
else:
    ans1 = ((-b) + complex(0, math.sqrt(-discriminant))) / (2 * a)
    ans2 = ((-b) - complex(0, math.sqrt(-discriminant))) / (2 * a)

if type(ans1) == complex or type(ans2) == complex:
    if ans1 == ans2:
        if ans1.imag >= 0:
            print("%.1f%+.1fi" % (round(ans1.real, 1), round(ans1.imag, 1)))
        else:
            print("%.1f%.1fi" % (round(ans1.real, 1), round(ans1.imag, 1)))
    else:
        if ans1.imag > ans2.imag:
            print("%.1f%+.1fi" % (round(ans1.real, 1), round(ans1.imag, 1)))
            print("%.1f%.1fi" % (round(ans2.real, 1), round(ans2.imag, 1)))
        else:
            print("%.1f%+.1fi" % (round(ans2.real, 1), round(ans2.imag, 1)))
            print("%.1f%.1fi" % (round(ans1.real, 1), round(ans1.imag, 1)))
else:
    if ans1 == ans2:
        print("%.1f" % ans1)
    else:
        print("%.1f" % ans1)
        print("%.1f" % ans2)
