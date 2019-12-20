# Import pandas
import pandas as pd
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
# Assign filename: file
file = 'titanic.csv'
# Import file: data
data = pd.read_csv(file, sep=',' , comment='#', na_values=['Nothing'])
# Print the head of the DataFrame
print(data.head(3))
# Plot 'Age' variable in a histogram
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()
