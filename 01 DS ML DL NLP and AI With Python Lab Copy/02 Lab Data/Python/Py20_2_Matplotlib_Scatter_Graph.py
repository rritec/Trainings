import matplotlib.pyplot as plt
# Import numpy as np
import numpy as np
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]
# Store pop as a numpy array: np_pop
np_pop = np.array(pop)
# To see clear size changes ,increase counts of  np_pop
np_pop = np_pop * 20
plt.scatter(year, pop,s = np_pop)
plt.xlabel('year')
plt.ylabel('population]')
plt.title('year wise population')
#Name the dots
plt.text(1950, 2.519, 'India')
plt.show()
