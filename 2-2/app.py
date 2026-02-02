import gradio as gr
import sqlite3

db_string = '/home/bigguy/Project-Files/class-code/Relational-Database-Sys/1-28_and_1-30/batting.db'


def fetch_phillies():
    conn = sqlite3.connect(db_string)
    cursor = conn.cursor()
    query = """
        SELECT playerID
        FROM batting
        WHERE yearID == 1976 AND teamID == 'PHI'
    """
    cursor.execute(query)
    records = cursor.fetchall()
    return_val = [record[0] for record in records]
    conn.close()
    return return_val

def fetch_player_hr_count(playerID):
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
    homeRuns = records[0][0]
    return f"# HOMERUNS FOR PLAYER: \n# {homeRuns}"

with gr.Blocks(title='APP') as dash:
    with gr.Row():
        dropdown = gr.Dropdown(choices=fetch_phillies())
        out = gr.Markdown()
    # with gr.Row():
    #     with gr.Column():
    for component in [dropdown]:
        component.change(fn=fetch_player_hr_count, inputs=[dropdown], outputs=[out])

dash.launch()