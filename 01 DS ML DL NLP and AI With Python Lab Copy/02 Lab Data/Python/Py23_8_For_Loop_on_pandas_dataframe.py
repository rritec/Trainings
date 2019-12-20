import pandas as pd
brics = pd.read_csv("brics.csv", index_col = 0)
print("******* 01. Column Names ********")
for val in brics :
    print(val)
print("******* 02 All rows ********")    
for lab, row in brics.iterrows() :
    print(lab)
    print(row)
print("******** 03 Selected Columns *********")
for lab, row in brics.iterrows() :
    print(lab + ": " + row["capital"]) 
print("******** 04 Add Column to result *********")
for lab, row in brics.iterrows() :
    brics.loc[lab, "name_length"] = len(row[ "country" ] )
print(brics)
print("******** 05 Another method to add Column to result *********")
brics["name_length1"] = brics["country"].apply(len)
print(brics)
