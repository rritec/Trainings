# Import package
from urllib.request import urlretrieve
import pandas as pd
# Assign url of file: url
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00192/BreastTissue.xls'
# Read in all sheets of Excel file: xl
xl = pd.read_excel(url, sheetname=None)
# Print the sheetnames to the shell
print(xl.keys())
# Print the head of the first sheet ,use sheet name: 'Data'
print(xl['Data'].head())
