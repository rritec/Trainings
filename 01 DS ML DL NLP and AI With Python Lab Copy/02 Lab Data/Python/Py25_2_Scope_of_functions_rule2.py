new_value = 10 # Global Variable

# Define function header 
def square(value):
    new_value = value ** 2  # Local Variable 
    print(new_value)

square(3) 
print(new_value) 