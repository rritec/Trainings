# Import pandas
import pandas as pd
# Assign spreadsheet filename: file
file = 'scottdata.xlsx'
# Load spreadsheet as: xl
xl = pd.exc
# Load a sheet into a DataFrame by name: EMP
df1 = xl.parse('EMP')
# Print the head of the DataFrame EMP
print(df1.head())
# Load a sheet into a DataFrame by index: DEPT
df2 = xl.parse(1)
# Print the head of the DataFrame df2
print(df2.head())
# Parse the first sheet and rename the columns: df3
df3 = xl.parse(0, skiprows=[0], names=['A', 'B','C','D','E','F','G','H'])
# Print the head of the DataFrame df3
print(df3.head(14))
# Parse the first column of the second sheet and rename the column: df4
df4 = xl.parse(1, parse_cols=[0], skiprows=[0], names=['A'])
# Print the head of the DataFrame df4
print(df4.head())