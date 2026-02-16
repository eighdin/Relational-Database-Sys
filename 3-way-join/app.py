import sqlite3
import pandas as pd
import gradio as gr

db_path = "/home/bigguy/Project-Files/class-code/Relational-Database-Sys/baseball.db"
players_query_path = "/home/bigguy/Project-Files/class-code/Relational-Database-Sys/3-way-join/top-10-hitters-alph.sql"

def run_sql(db_path, query_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    with open(query_path) as file:
        query = file.read()
        cursor.execute(query)
    records = cursor.fetchall()
    return records

def f(x):
    pass

with gr.Blocks() as display:
    players = [player[0] for player in run_sql(db_path, players_query_path)]
    with gr.Row():
        dropdown = gr.Dropdown(choices=players)
        out = gr.Markdown()
    for component in [dropdown]:
        component.change(fn=f, inputs=[dropdown], outputs=[out])

display.launch()
