def raise_val(n):
    """Return the inner function."""
    def inner(x):
        """Raise x to the power of n."""
        raised = x ** n
        return raised
    return inner
square = raise_val(2)
print(square(3))
