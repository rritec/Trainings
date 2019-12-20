new_value = 10 # Global Variable
print(new_value)
# Define function header 
def square(value):
    global new_value
    new_value = value ** 2  
    print(new_value)

square(3) 
print(new_value) 