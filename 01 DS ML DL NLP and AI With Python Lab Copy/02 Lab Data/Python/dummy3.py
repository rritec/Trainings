def sqrt(x):
    """ Return the square root of a number."""
    if x < 0:
        raise ValueError('x must be non-integer')
    else:
        print(x ** 0.5)
sqrt(-9)
        
        