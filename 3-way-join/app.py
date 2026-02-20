import sqlite3
import pandas as pd
import gradio as gr

db_path = "/home/bigguy/Project-Files/class-code/Relational-Database-Sys/baseball.db"
players_query_path = "/home/bigguy/Project-Files/class-code/Relational-Database-Sys/3-way-join/top-10-hitters-alph.sql"
hr_by_yr_query_path = "/home/bigguy/Project-Files/class-code/Relational-Database-Sys/3-way-join/get-hrs-by-yr.sql"

def run_sql(db_path, query_path, param=None):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    with open(query_path) as file:
        query = file.read()
        if param != None:
            cursor.execute(query, [param])
        else:
            cursor.execute(query)
    records = cursor.fetchall()
    return records

def player_hr_by_yr(playerID):
    records = run_sql(db_path, hr_by_yr_query_path, playerID)
    records_df = pd.DataFrame(records, columns=['Year', 'HRs'])
    records_df['Year'] = records_df["Year"].astype(str)
    return records_df

with gr.Blocks() as display:
    players = run_sql(db_path, players_query_path)
    with gr.Row():
        dropdown = gr.Dropdown(choices=players)
    out = gr.LinePlot(x='Year', y='HRs')
    for component in [dropdown]:
        component.change(fn=player_hr_by_yr, inputs=[dropdown], outputs=[out])

display.launch()