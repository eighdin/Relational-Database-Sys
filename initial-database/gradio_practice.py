import gradio as gr
import sqlite3
import pandas as pd

def return_table():

    conn = sqlite3.connect('points.db')
    cursor = conn.cursor()

    query_file = open('get_table.sql', 'r')
    query = query_file.read()
    query_file.close()

    cursor.execute(query)
    points = cursor.fetchall()
    conn.close()

    points_df = pd.DataFrame(points, columns=['id', 'x', 'y'])
    output = points_df
    
    return output

with gr.Blocks() as display:
    df = return_table()
    with gr.Row():
        gr.Label(len(df), label='Point Count')
        gr.Label(df['x'].min(), label='Lowest X')
    gr.DataFrame(df)

display.launch()