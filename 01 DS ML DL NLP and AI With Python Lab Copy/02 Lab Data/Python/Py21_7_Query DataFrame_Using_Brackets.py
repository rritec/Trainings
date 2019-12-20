# Import pandas as pd
import pandas as pd
# import csv file
cars = pd.read_csv('cars.csv', index_col = 0)
# Query country column as Pandas Series
print(cars['country'])
# Query country column as Pandas DataFrame
print(cars[['country']])
# Query DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])
# Print out first 3 observations
print(cars[0:3])
# Print out fourth, fifth and sixth observation
print(cars[3:6])
