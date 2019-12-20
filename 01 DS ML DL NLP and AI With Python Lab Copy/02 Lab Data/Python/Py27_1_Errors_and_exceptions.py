def sqrt(x):
    """Returns the square root of a number."""
    try:
        print(x ** 0.5)
    except:
        print('x must be an int or float')
print("***** 01 Execute with integer value******")
sqrt(9)
print("***** 02 Execute with string value******")
sqrt("ABCD")
