# Create a list of strings: names
names = ['Ram', 'Rabson', 'Robert', 'Nancy']
# Print each list item in names list using a for loop
print("****** 01 For Loop Output ******")
for person in names:
    print(person)
print("****** 02 Replicate for loop output with list_iterator Output ******")
# Create an iterator for names list: avoid_for
avoid_for = names.__iter__() # or iter(names)
print(type(avoid_for))
# Print each item from the iterator
print(next(avoid_for))
print(next(avoid_for))
print(next(avoid_for))
print(next(avoid_for))
