# Import pandas
import pandas as pd
# Read data from csv files
df1 = pd.read_csv('Py_cleaning_pivot_concat1.csv')
df2 = pd.read_csv('Py_cleaning_pivot_concat2.csv')
print("***** 01. Observe first data frame *****")
print(df1)
print("***** 02. Observe second data frame *****")
print(df2)
print("****** 03. Observe concatenated data frame *******")
concatenated = pd.concat([df1, df2])
print(concatenated)
print("****** 04. Observe that indexes are duplicated  *******")
print(concatenated.loc[0, :])
print("****** 05. concatenat without indexes are duplicated  *******")
concatenated = pd.concat([df1, df2],ignore_index=True)
print(concatenated)


