import pandas as pd
import sqlite3

df = pd.read_csv('./1-28_and_1-30/batting.csv')

conn = sqlite3.connect('batting.db')
cursor = conn.cursor()
df.to_sql('batting', conn, if_exists='replace', index=False)
conn.commit()
conn.close()
