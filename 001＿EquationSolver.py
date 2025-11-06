a = int(input())
b = int(input())
c = int(input())

ans1 = ((b * -1) + (b**2 - 4 * a * c) ** 0.5) / (2 * a)
ans2 = ((b * -1) - (b**2 - 4 * a * c) ** 0.5) / (2 * a)

if type(ans1) == complex or type(ans2) == complex:
    print("It's not real")
    if ans1 == ans2:
        ans1rounded = round(ans1.real, 1) + round(ans1.imag, 1) *1j
        print(ans1rounded)
    else:
        ans1rounded = round(ans1.real, 1) + round(ans1.imag, 1) *1j
        ans2rounded = round(ans2.real, 1) + round(ans2.imag, 1) *1j
else:
    if ans1 == ans2:
        print("%.1f" % ans1)
    else:
        print("%.1f" % ans1)
        print("%.1f" % ans2)

print(ans1, ans2)