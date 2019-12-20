# Import the NumPy package
import numpy
#Creating NumPy 2D Array
np_2d_array = numpy.array([[1.71, 1.58, 1.51, 1.73, 1.92],[65.9, 58.8, 66.8, 83.4, 68.7]])
print(type(np_2d_array))
# Dimensions of array (rows and columns)
print(np_2d_array.shape)
# Reading 2D Array elements 
print(np_2d_array[0])  # 1 row of elements
print(np_2d_array[0][2]) # 1 row 3 column element
print(np_2d_array[:,0:2]) # All rows and 1st ,2nd columns
print(np_2d_array[1,:]) # All columns and 2nd row