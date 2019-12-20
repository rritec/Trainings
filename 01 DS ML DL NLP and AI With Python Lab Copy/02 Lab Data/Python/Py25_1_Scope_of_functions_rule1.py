# Define function header 
def square(value):
    new_value = value ** 2  # Local Variable 
    print(new_value)
    
square(10) 
print(new_value) #Error: NameError: name 'new_value' is not defined
