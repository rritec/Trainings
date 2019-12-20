# Import necessary module sqlalchemy
from sqlalchemy import create_engine
# Create Python engine: engine for SQLite database
engine = create_engine('sqlite:///Chinook.sqlite')
# Save the table names to a list object : table_names
table_names = engine.table_names()
# Print the table names on console
print(table_names)