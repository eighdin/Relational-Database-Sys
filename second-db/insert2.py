import sqlite3

conn = sqlite3.connect('playoffs.db')
cursor = conn.cursor()

query_file = open('queryinsert.sql', 'r')
query = query_file.read()
query_file.close()

cursor.execute(query)
conn.commit()
conn.close()