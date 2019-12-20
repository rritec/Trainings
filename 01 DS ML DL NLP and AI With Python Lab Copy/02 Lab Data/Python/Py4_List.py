# Define  a list with same data types
rritec_emp_sal=[1000,2000,3000,4000]
print(rritec_emp_sal)
print(type(rritec_emp_sal))
# Define  a list with different data types
rritec_emp_name_sal=["ram",1000,"nancy",2000,"robert",3000,"rabson",4000]
print(rritec_emp_name_sal)
# A list may contain other list
rritec_emp_name_sal1=[["ram",1000],["nancy",2000],["robert",3000],["rabson",4000]]
print(rritec_emp_name_sal1)
print(type(rritec_emp_name_sal1))
# Read list values (Slicing and dicing)
print(rritec_emp_name_sal[0])
print(rritec_emp_name_sal[-1])
print(rritec_emp_name_sal[0:4])
print(rritec_emp_name_sal[:4])
print(rritec_emp_name_sal[4:])
print(rritec_emp_name_sal1[0][0])
print(rritec_emp_name_sal1[0][-1])
##### Manipulating lists
# Changing list value
rritec_emp_name_sal[0]='Ram Reddy'
rritec_emp_name_sal[2:4]=['willis',2100]
print(rritec_emp_name_sal)
# Adding Elements
rritec_emp_name_sal=rritec_emp_name_sal + ['Helen',5000]
print(rritec_emp_name_sal)
# Deleting  Elements
del(rritec_emp_name_sal[2:4])
print(rritec_emp_name_sal)
# Need to observe 1
x = [1000,2000,3000]
y = x
z = list(x)
y[0]=1001
print(y)
print(x)
# Need to observe 2
x = [1000,2000,3000]
z = list(x)
z[1] = 2001
print(z)
print(x)


