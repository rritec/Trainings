# Dictionary of dictionaries
world = {"China":{'Capital':'Beijing','Population':1.38},\
         "India":{'Capital':'New Delhi','Population':1.34},\
         "USA":{'Capital':'Washington, D.C','Population':0.32}}
# Print out the capital of India
print(world['India']['Capital'])
# Create sub-dictionary data
data = { 'capital':'rome', 'population':59.83 }
# Add data to world under key 'italy'
world['italy'] = data
# Print world
print(world)