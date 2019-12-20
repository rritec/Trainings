nums = [3, 6, 4, 10, 1]
""" Function map takes two arguments: map(func, seq)
map() applies the function to all elements in the sequence"""
square_all = filter(lambda num:  num>5,nums)
print(square_all)
print(list(square_all))
