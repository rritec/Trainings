#import required modules 
import numpy as np
# define list of family members height $ weight
np_family_heights = np.array([1.73, 1.68, 1.71, 1.89])
np_family_weights = np.array([70, 60, 65, 80])
#Define 2D numpy array
np_family_heights_weights = np.array([np_family_heights,np_family_weights])
# Define for loop using nditer function
for height in np.nditer(np_family_heights_weights) :
    print(height)
    
    