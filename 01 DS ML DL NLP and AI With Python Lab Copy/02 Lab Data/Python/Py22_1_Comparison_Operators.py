print("01. Comparison of booleans")
print(True == False)
print(True != False)

print("02. Comparison of integers")
print(-5 * 15 != 75)
print(2 == (1 + 1))

print("03. Comparison of strings")
print("R" != "python")
print("Python" != "python") # note P is capital

print("04. Compare a boolean with a numeric")
print(True == 1)

print("05. Compare numpy list with integer")
import numpy as np
marks = np.array([10,20,30,40,50,60,70,80,90,100])
print(marks>50)
print(marks[marks>50])

#remove comment and execute what you noticed?
#print("06. Compare python list with integer")
#print([10,20,30,40,50,60,70,80,90,100]>50) 
#print("07. Compare int with string")
#print(1<"RAM")



