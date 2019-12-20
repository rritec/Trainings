import pandas as pd
df = pd.read_csv('emp_missing.csv')
# Print info of df
print(df.info())
# Calculate the mean of the comm column : comm_mean
COMM_mean = round(df.COMM.mean(),1)
# Replace all the missing values in the comm column with the mean
df['COMM'] = df.COMM.fillna(COMM_mean)
# Print the info
print(df.info())
print(df)
print("****** drop missing values rows ******")
df_dropped = df.dropna(axis = 0) # use axis = 1 to drop columns
df_dropped.info()



