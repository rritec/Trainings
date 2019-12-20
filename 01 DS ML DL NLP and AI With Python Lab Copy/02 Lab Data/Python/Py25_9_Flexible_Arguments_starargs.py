def add_all(*args):
    """Sum all values in *args together."""
    # Initialize sum
    sum_all = 0
    # Accumulate the sum
    for num in args:
        sum_all += num
    return sum_all
    
print(add_all(1,2,3))
print(add_all(10,20,30,40,50))

