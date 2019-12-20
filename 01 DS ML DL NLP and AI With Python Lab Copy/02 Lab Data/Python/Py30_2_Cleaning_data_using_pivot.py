# Import pandas
import pandas as pd
# Read the file into a DataFrame: df
df = pd.read_csv('Py_cleaning_pivot_data.csv')
print("****** 01. data before pivoting *******")
print(df)
print("****** 02. data after pivoting *******")
df_pivot = df.pivot(index='name',columns='treatment',values='result')
print(df_pivot)
