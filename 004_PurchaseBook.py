BookPrice = {"A": 440, "B": 1200, "C": 130}
bookAAmmount = int(input())
bookBAmmount = int(input())
bookCAmmount = int(input())

totalPrice = (
    BookPrice["A"] * bookAAmmount
    + BookPrice["B"] * bookBAmmount
    + BookPrice["C"] * bookCAmmount
)
print(totalPrice)
