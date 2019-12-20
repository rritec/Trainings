# Import pandas
import pandas as pd
# Read the file into a DataFrame: df
df = pd.read_csv('Py_cleaning_Tidydata.csv')
print("data before melting")
print(df)
print("melt and print data")
df_melt = pd.melt(frame=df, id_vars='name',value_vars=['treatment a', 'treatment b'],\
              var_name='treatment', value_name='result')
print(df_melt)


"""
#import required packages
import pandas as pd
# read csv file and load as DataFrame
df = pd.read_csv("Py_cleaning_Tidydata1.csv")
#observe data
print(df)
print ("******************after melt*************")
#wrong data as values (treatment a and b are acting as variables
df_melt = pd.melt(frame = df,id_vars = 'treatment', value_vars = ["John Smith","Jane Doe","Mary Johnson"] ,\
                  var_name = "name", value_name ="result")
print(df_melt)
""""

