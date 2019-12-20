#import required packages
import glob
import pandas as pd
print("***** 01. Read all emp_part files from working directory *****")
csv_files = glob.glob('emp_part?.csv')
print(csv_files)
# Create an empty list: emp_list
emp_list = []
#  Iterate over csv_files
for csv in csv_files:
    #  Read csv into a DataFrame: df
    df = pd.read_csv(csv)  
    # Append df to emp_list
    emp_list.append(df)
# Concatenate emp_list into a single DataFrame: emp
emp = pd.concat(emp_list)
print("***** 02. print after combining files  *****")
print(emp)


