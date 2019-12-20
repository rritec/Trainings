import pandas as pd
df = pd.read_csv('emp_duplicate.csv')
# Print info of df
print(df.info())
# Drop the duplicates: df_no_duplicates
df_no_duplicates = df.drop_duplicates()
# Print info of tracks_no_duplicates
print(df_no_duplicates.info())



