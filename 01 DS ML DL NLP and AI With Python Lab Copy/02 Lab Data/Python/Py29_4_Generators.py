# List of strings
std = ['Ram Reddy', 'Rabson', 'Robert', 'Nancy']
# List comprehension
std1 = [member for member in std if len(member) > 5]
print(type(std1))
print(std1)
# Generator expression
std2 = (member for member in std if len(member) > 5)
print(type(std2))
print(std2)
