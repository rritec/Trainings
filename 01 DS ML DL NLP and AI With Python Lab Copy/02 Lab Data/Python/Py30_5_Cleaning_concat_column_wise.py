# Import pandas
import pandas as pd
# Read data from csv files
df1 = pd.read_csv('Py_cleaning_pivot_concat3.csv')
df2 = pd.read_csv('Py_cleaning_pivot_concat4.csv')
print("***** 01. Observe first data frame *****")
print(df1)
print("***** 02. Observe second data frame *****")
print(df2)
print("****** 03. Observe concatenated data frame column wise*******")
concatenated = pd.concat([df1, df2],axis=1)
print(concatenated)




