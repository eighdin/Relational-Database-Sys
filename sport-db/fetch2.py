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
records_df['city_char_counts'] = records_df['city'].str.len()
records_df['team_char_counts'] = records_df['name'].str.len()
records_df['length_tuples'] = tuple(zip(records_df['city_char_counts'], records_df['team_char_counts']))
output = records_df['length_tuples'].to_list()

print(output)