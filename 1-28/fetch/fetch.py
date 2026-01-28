import sqlite3
import pandas as pd

conn = sqlite3.connect('batting.db')
cursor = conn.cursor()
with open('./fetch/fetch_query.sql', 'r') as query_file:
    cursor.execute(query_file.read())

records = cursor.fetchall()
conn.close()

df = pd.DataFrame(records, columns=['playerID', 'teamID', 'yearID', 'HR'])
outlist = pd.DataFrame(columns=['Year', 'Count'])
for year in df['yearID']:
    if year in outlist['Year'].values:
        outlist.loc[outlist['Year'] == year, 'Count'] += 1
    else:
        outlist.loc[len(df)] = [year, 1]

print(df['yearID'])
