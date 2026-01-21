import sqlite3
import pandas as pd

conn = sqlite3.connect('playoffs.db')
cursor = conn.cursor()

query_file = open('queryfetch.sql', 'r')
query = query_file.read()
query_file.close()

cursor.execute(query)
records = cursor.fetchall()
conn.close()

records_df = pd.DataFrame(records, columns = ['id', 'city', 'name'])
print(records_df['city'])