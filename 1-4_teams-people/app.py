import sqlite3
import pandas as pd

# top 10 player career hrs
player_career_hr_query = '/home/bigguy/Project-Files/class-code/Relational-Database-Sys/1-4_teams-people/top-career-hrs.sql'
# Philly homeruns by year
phi_hrs_by_yr = '/home/bigguy/Project-Files/class-code/Relational-Database-Sys/1-4_teams-people/yr-by-yr_philly_hrs.sql'

conn = sqlite3.connect('baseball.db')
cursor = conn.cursor()
query = None
with open(phi_hrs_by_yr, 'r') as file:
    query = file.read()
cursor.execute(query)
records = cursor.fetchall()
conn.close()

print(pd.DataFrame(records, columns=['yearID', 'Career HRs']))