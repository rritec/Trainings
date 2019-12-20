# Import package
import numpy as np
# Assign filename to variable: file
file = 'mnist_digits.csv'
# Load file as array: digits
digits = np.loadtxt(file, delimiter=',')
# Print datatype of digits
print(type(digits))
# Select and reshape a row
im = digits[21, 1:]
print(im.shape)
im_sq = np.reshape(im, (28, 28))
import matplotlib.pyplot as plt
# Plot reshaped data (matplotlib.pyplot already loaded as plt)
plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()
np.load