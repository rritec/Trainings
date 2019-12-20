# Create a list of strings: DataScience
DataScience = ['PYTHON','MATHS','STATS','ML','AI']
print("***** 01. enumerate() function creates enumarate object *****")
print(enumerate(DataScience))
print( "***** 02. Create a list of tuples ***** ")
DataScience_list = list(enumerate(DataScience))
print(type(DataScience_list))
# Print the list of tuples
print(DataScience_list)
print("***** 03. Unpack and print the tuple pairs *****")
for index1, value1 in enumerate(DataScience):
    print(index1, value1)
print("***** 04. Unpack and print with given  start index *****")
for index2, value2 in enumerate(DataScience, start=1):
    print(index2, value2)
    
