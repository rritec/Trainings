def mod2plus5(x1, x2, x3):
    """Returns the remainder plus 5 of three values."""
    def inner(x):
        """Returns the remainder plus 5 of a value."""
        return x % 2 + 5
    return (inner(x1), inner(x2), inner(x3))

print(mod2plus5(2,3,4))


