# Step 1 of 7: Import required packages
from sqlalchemy import create_engine
import pandas as pd
# Step 2 of 7: Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')
# Step 3 of 7: Open engine connection
con = engine.connect()
# Step 4 of 7: Perform query: result
result = con.execute("SELECT * FROM Album")
# Step 5 of 7: Save results of the query to DataFrame: df
df = pd.DataFrame(result.fetchall())
# Step 6 of 7: Close connection
con.close()
# Step 7 of 7: Print head of DataFrame df
print(df.head())
