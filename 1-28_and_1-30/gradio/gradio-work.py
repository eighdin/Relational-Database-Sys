import sqlite3
import pandas as pd
import gradio as gr
db_string = '/home/bigguy/Project-Files/class-code/Relational-Database-Sys/1-28_and_1-30/batting.db'

def fetch_phillies():
    conn = sqlite3.connect(db_string)
    cursor = conn.cursor()
    with open('/home/bigguy/Project-Files/class-code/Relational-Database-Sys/1-28_and_1-30/gradio/fetch_query_phillyplayers.sql', 'r') as query_file:
        cursor.execute(query_file.read())

    records = cursor.fetchall()
    return_val = [record[0] for record in records]
    conn.close()
    return return_val

def getHRsforPlayer(playerID):
    conn = sqlite3.connect(db_string)
    cursor = conn.cursor()
    query = f"""
        SELECT hr
        FROM batting
        WHERE playerID == ? AND yearID == 1976 AND teamID == 'PHI'
    """
    cursor.execute(query, [playerID])
    records = cursor.fetchall()
    conn.close()
    print(records)
    homeRuns = records[0][0]
    return homeRuns

iface = gr.Interface(fn = getHRsforPlayer, inputs=gr.Dropdown(choices=fetch_phillies()), outputs = 'number')

iface.launch()

# df = pd.DataFrame(records, columns=['playerID', 'teamID', 'yearID', 'HR'])
# outlist = pd.DataFrame(columns=['Year', 'Count'])
# for year in df['yearID']:
#     if year in outlist['Year'].values:
#         outlist.loc[outlist['Year'] == year, 'Count'] += 1
#     else:
#         outlist.loc[len(df)] = [year, 1]

# print(df['yearID'])
