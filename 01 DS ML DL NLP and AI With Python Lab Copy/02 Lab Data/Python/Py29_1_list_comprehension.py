print("01. Using for loop to add 5 to list items")
nums = [10,20,30,40,50]
new_nums = []
for num in nums:
    new_nums.append(num+5)
print(new_nums)
print("02. Using list comprehension to add 5 to list items")
new_nums1 = [num + 5 for num in nums]
print(new_nums1)
print("03. Using List comprehension with range")
result = [num for num in range(11)]
print(result)