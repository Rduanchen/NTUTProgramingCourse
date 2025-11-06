def calculate_bmi(height, weight):
    return weight / (height) ** 2


def grading(bmi):
    if bmi >= 35:
        return "Severe obesity"
    elif bmi >= 30:
        return "Moderate obesity"
    elif bmi >= 27:
        return "Mild obesity"
    elif bmi >= 24:
        return "Overweight"
    elif bmi >= 18:
        return "Normal"
    elif bmi < 18:
        return "Underweight"


h = float(input())
w = int(input())
print(grading(calculate_bmi(h, w)))
