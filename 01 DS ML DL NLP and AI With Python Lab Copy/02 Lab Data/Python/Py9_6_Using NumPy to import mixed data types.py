# Import package
import numpy as np
# Assign filename to variable: file
file = 'emp.txt'
# Load file as array: emp
emp = np.genfromtxt('emp.txt', delimiter=',', names=True, dtype=None)
# Print datatype of emp
print(type(emp)) #<class 'numpy.ndarray'>
print(emp)  # all data 
print("shape")
print(np.shape(emp)) # (14,)
print("sal column")
print(emp['SAL'])
#Import matplotlib library
import matplotlib.pyplot as plt
# Plot a scatter plot of the data
plt.scatter(emp['COMM'], emp['SAL'])
plt.xlabel('Comm')
plt.ylabel('Sal')
plt.show()