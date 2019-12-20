# Create a list of tuples
std_no = (10,20,30)
std_name = ("Ram","Nancy","Rabson")
std_marks = (100,2000,300)
#create zip object
std_data = zip(std_no, std_name, std_marks)
print("***** 01. Print the list of tuples create by zip function *****")
print(type(std_data))
print(std_data)
print(list(std_data))
print("***** 02. Unpack the zip object and print the tuple values *****")
std_data1 = zip(std_no, std_name, std_marks)
for value1, value2, value3 in std_data1:
    print(value1, value2, value3)
    