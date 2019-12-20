print("01. nested loops ")
pairs_1 = []
for num1 in range(0, 2):
    for num2 in range(6, 8):
        pairs_1.append((num1, num2))
print(pairs_1)
print("02. nested loops using list comprehension ")
pairs_2 = [(num1, num2) for num1 in range(0, 2) for num2
in range(6, 8)]
print(pairs_2)