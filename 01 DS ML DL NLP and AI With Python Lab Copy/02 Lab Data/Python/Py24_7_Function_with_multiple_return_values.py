# Define function header 
def raise_both(value1,value2):
    """Raise value1 to the power of value2
    and vice versa."""
    new_value1 = value1 ** value2
    new_value2 = value2 ** value1
    new_tuple = (new_value1,new_value2)
    return new_tuple
# Call the function
rs = raise_both(10,2)
print(rs)  

