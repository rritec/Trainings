# Import pandas package
import pandas as pd
# Import matplotlib package
import matplotlib.pyplot as plt




# Import sas7bdat package
from sas7bdat import SAS7BDAT  # or import sas7bdat as sas



# Save file to a DataFrame: df_sas
with SAS7BDAT('cars.sas7bdat') as file:
    df_sas = file.to_data_frame()
# Print head of DataFrame
print(df_sas.head())
# Plot histograms of a DataFrame
#pd.DataFrame.hist(df_sas[['P']])
#plt.ylabel('count')
#plt.show()
