# Loop over range(5) and print the values
print("****** 01 For Loop Output ******")
for num in range(5):
    print(num)

# Create an iterator for range(5): range_iterator
print("****** 02 Replicate for loop output with range_iterator Output ******")
range_iterator = iter(range(5))
print(type(range_iterator))

# Print the values in range_iterator
print(next(range_iterator))
print(next(range_iterator))
print(next(range_iterator))
print(next(range_iterator))
print(next(range_iterator))


