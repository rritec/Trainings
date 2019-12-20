#Create dictionary
world = {"China":1.38,"India":1.34,"USA":0.32}
#print data type
print(world)
# Add one item to Dictionary
world["Indonesia"]=0.26
world["Brazil"]=0.21
#Indonesia available in world dictionary
print('Indonesia' in world)
print(world)
# update one item of world Dictionary
world["India"]=1.39
print(world)
# delete one item of world Dictionary
del(world["Brazil"])
print(world)