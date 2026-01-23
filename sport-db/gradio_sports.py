import gradio as gr
import sqlite3
import pandas as pd

def return_table():

    conn = sqlite3.connect('playoffs.db')
    cursor = conn.cursor()

    query_file = open('queryfetch.sql', 'r')
    query = query_file.read()
    query_file.close()

    cursor.execute(query)
    sports = cursor.fetchall()
    conn.close()

    sport_df = pd.DataFrame(sports, columns=['id', 'city', 'name'])
    output = sport_df
    
    return output

with gr.Blocks() as display:
    df = return_table()
    with gr.Row():
        gr.Label(len(df), label='Team Count')
        gr.Label(df['city'].sort_values(ascending=True)[0], label='Last City Alphabetically')
    gr.DataFrame(df)

display.launch()