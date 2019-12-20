# Import required packages
from urllib.request import urlretrieve
import pandas as pd
# Assign url of file: url_of_file
url_of_file = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
# Save file locally into working directory
urlretrieve(url_of_file, 'winequality-red.csv')
# Read file into a DataFrame and print its head
df = pd.read_csv('winequality-red.csv', sep=';')
print(df.head())
