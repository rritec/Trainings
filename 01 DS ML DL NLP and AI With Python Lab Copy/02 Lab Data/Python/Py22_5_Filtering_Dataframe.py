print("01. Import csv file as pandas dataframe")
import pandas as pd
brics = pd.read_csv("brics.csv", index_col = 0)
print(brics)

print("02. observe area column")
print(brics["area"]) # try brics.loc[:,"area"] or brics.iloc[:,2]

print("03. filter data area >8 ")
print(brics[brics["area"] > 8])

print("04. filter data using boolean operator")
import numpy as np
print(brics[np.logical_and(brics["area"] > 8, brics["area"] < 10)])