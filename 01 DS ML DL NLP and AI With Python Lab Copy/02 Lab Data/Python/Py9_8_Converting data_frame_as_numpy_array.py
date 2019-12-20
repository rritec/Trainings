import pandas as pd
# Assign the filename: file
file = 'emp.csv'
# Read the first 3 rows of the file into a DataFrame: emp
emp = pd.read_csv(file, nrows=3, header=None)
# Build a numpy array from the DataFrame: emp
emp_array = emp.values
# Print the datatype of data_array to the shell
print(type(emp_array))  #<class 'numpy.ndarray'>
print(emp_array)
print(emp_array[1][0])