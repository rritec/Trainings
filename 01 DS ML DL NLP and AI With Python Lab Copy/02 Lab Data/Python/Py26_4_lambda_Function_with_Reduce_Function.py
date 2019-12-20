"""# Define meaningless function
def meaningless(*args):
    # Concatenate strings in *args together.
    hodgepodge = ''
    for word in args:
        hodgepodge += word
    return hodgepodge
print(meaningless('ram', 'reddy', 'nancy', 'robert', 'robson'))"""
#Above code can be replicated with below lambda function 
# Import reduce from functools
from functools import reduce
# Create a list of strings: stark
stark = ['ram', 'reddy', 'nancy', 'robert', 'robson']
# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda item1, item2: item1 + item2, stark)
# Print the result
print(result)
