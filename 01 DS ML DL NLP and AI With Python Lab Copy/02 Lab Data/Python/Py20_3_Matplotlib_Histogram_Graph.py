#import required packages
import matplotlib.pyplot as plt
# define 1 to 100 prime numbers as a list
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,\
          53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
#plot histogram
plt.hist(values, bins = 5) 
plt.show()
#clear plot
plt.clf()
#plot histogram
plt.hist(values) # default value of bins is 10
plt.show()
plt.clf()