# Define list of lists
house = [["Hall area", 11.25], 
         ["Kitchen area", 18.0], 
         ["Living room area", 20.0], 
         ["Bedroom area", 10.75], 
         ["Bathroom area ", 9.50]]         
# Build a for loop
for x in house :
    print("The " + str(x[0]) + " is " + str(x[1]) + " sqm")