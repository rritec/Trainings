# Import pandas
import pandas as pd
import numpy as np
# Read the file into a DataFrame: df
df = pd.read_csv('Py_cleaning_pivot_data1.csv')
print("****** 01. data before pivoting *******")
print(df)
print("****** 02. data after pivoting *******")
df_pivot = df.pivot_table(values='value',index='date',columns='temperature',aggfunc=np.mean)
print(df_pivot)
