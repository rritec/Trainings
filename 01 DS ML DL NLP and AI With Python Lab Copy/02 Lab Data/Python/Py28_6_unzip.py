std_name = ("Ram","Nancy","Rabson")
std_course = ("R","PYTHON","DATASCIENCE")
# Create a zip object : z1
z1 = zip(std_course, std_name)
print("01. tuples in z1 after unpacking with *")
print(*z1)
# Re-create a zip object : z1
z1 = zip(std_course, std_name)
# 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
result1, result2 = zip(*z1)
print("02. Check if unpacked tuples are equivalent to original tuples")
print(result1 == std_course)
print(result2 == std_name)



