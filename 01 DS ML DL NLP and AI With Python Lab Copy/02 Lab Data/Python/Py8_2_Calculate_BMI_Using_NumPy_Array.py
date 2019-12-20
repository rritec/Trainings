# Create list of heights of students
height = [1.71, 1.58, 1.51, 1.73, 1.92]
# Create list of weights of students
weight = [65.9, 58.8, 66.8, 83.4, 68.7]
# Import the NumPy package
import numpy
# Create a NumPy array
np_height = numpy.array(height)
np_weight = numpy.array(weight)
# Print out type of np_height
print(type(np_height))
print(type(np_weight))
#calculate Body Mass Index(BMI)
BMI=np_weight/np_height **2
print(BMI)
# Reading BMI
print(BMI[1]) # Reading one element of array
print(BMI[1:3]) # Reading subset of array
print(BMI[BMI>28]) #Reading Array based on Condition