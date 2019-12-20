# Create generator object: result
result = (num for num in range(10))
print("***** 01 First 5 values of generator ***** ")
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print("***** 02 Print the rest of the values using for Loop *****")

for value in result:
    print(value)
    
