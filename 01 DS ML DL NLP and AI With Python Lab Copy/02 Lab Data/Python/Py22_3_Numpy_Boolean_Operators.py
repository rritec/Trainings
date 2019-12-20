print("01. logical_and() Boolean operator")
import numpy as np
marks = np.array([10,20,30,40,50,60,70,80,90,100])
print(np.logical_and(marks>50,marks<80))
      
print("02. logical_or() Boolean operator")
marks = np.array([10,20,30,40,50,60,70,80,90,100])
print(np.logical_or(marks==50,marks>70))

print("03. logical_not() Boolean operator")
marks = np.array([10,20,30,40,50,60,70,80,90,100])
print(np.logical_not(marks==50))



