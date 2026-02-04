import pandas as pd
import sqlite3

people_table = pd.read_csv('people.csv')
teams_table = pd.read_csv('teams.csv')

conn = sqlite3.connect('baseball.db')
cursor = conn.cursor()
people_table.to_sql('people', conn, if_exists='replace', index=False)
teams_table.to_sql('teams', conn, if_exists='replace', index=False)
conn.commit()
conn.close()
