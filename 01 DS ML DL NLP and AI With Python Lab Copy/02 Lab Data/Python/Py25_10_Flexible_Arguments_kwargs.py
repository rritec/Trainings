def print_all(**kwargs):
    """Print out key-value pairs in **kwargs."""
    # Print out the key-value pairs
    for key, value in kwargs.items():
        print(key + ": " + value)
print_all(student1="Rabson", student2="Robert",student3 ="Ram Reddy",student4="Nancy")
