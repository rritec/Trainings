# Pre-defined lists
country_names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
drives_right =  [True, False, False, False, True, True, True]
cars_avg_per_1000 = [809, 731, 588, 18, 200, 70, 45]
# Import pandas as pd
import pandas as pd
# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = { 'country':country_names,\
            'drives_right':drives_right,\
            'cars_per_1000':cars_avg_per_1000 }
# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)
# Definition of row_labels
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']
# Specify row labels of cars
cars.index = row_labels
# Print cars again
print(cars)
