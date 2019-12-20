#list comprehension with if statement
print([num ** 2 for num in range(10) if num % 2 == 0])
print([num ** 2 if num % 2 == 0 else 0 for num in range(10)])
print("positive and negative numbers")
pos_neg = {num: -num for num in range(10)}
print(pos_neg)
print(type(pos_neg))
