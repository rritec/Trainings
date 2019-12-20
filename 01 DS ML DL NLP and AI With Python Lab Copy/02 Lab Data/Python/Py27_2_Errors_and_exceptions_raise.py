def sqrt(x):
    """Returns the square root of a number."""
    if x < 0:
        raise ValueError('x must be non-negative')
    else:
        print(x ** 0.5)
    
print("***** 01 Execute with integer value******")
sqrt(9)
print("***** 02 Execute with negative value******")
sqrt(-9)