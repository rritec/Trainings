import pandas as pd
df = pd.read_csv('tips.csv')
print("***** 01. Observe the info of data frame and note down memory *****")
df.info()
# Convert the sex column to type 'category'
df.sex = df.sex.astype('category')
# Convert the smoker column to type 'category'
df.smoker = df.smoker.astype('category')
# Convert 'total_bill' to a numeric dtype
df['total_bill'] = pd.to_numeric(df['total_bill'], errors='coerce')
# Convert 'tip' to a numeric dtype
df['tip'] = pd.to_numeric(df['tip'], errors='coerce')
print("***** 02. Observe the info of data frame and note down memory *****")
df.info()
print("***** 03. did you observed memory difference *******")
print("***** 04. did you observed - replaced with NaN *******")
print(df)
