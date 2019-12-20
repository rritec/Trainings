import pandas as pd
df = pd.read_csv('emp_missing.csv')
print("****** drop missing values rows ******")
df_dropped = df.dropna(axis = 0) # use axis = 1 to drop columns
df_dropped.info()
# Assert that there are no missing values
assert pd.notnull(df_dropped).all().all()
# Assert that all values are >= 0
assert (df_dropped >= 0).all().all()
#observe data
print(df_dropped)










