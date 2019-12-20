# Import pandas
import pandas as pd
# Assign the filename: file
file = 'emp.csv'
# Read the file into a DataFrame: emp
emp= pd.read_csv(file)
# View the head of the DataFrame
#print(emp.head(14))
print(emp[['SAL']])