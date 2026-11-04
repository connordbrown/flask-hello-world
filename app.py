from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! \n- from Connor Brown in CSPB 3308'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://flask_hello_world_bv1f_user:dZptydDRnBXx2MA0QHJOfvznAeDK0orH@dpg-dblq2415efls73afdbn0-a/flask_hello_world_bv1f")
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def db_create():
    conn = psycopg2.connect("postgresql://flask_hello_world_bv1f_user:dZptydDRnBXx2MA0QHJOfvznAeDK0orH@dpg-dblq2415efls73afdbn0-a/flask_hello_world_bv1f")
    curr = conn.cursor()
    curr.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
            );
            ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"

@app.route('/db_insert')
def db_insert():
    conn = psycopg2.connect("postgresql://flask_hello_world_bv1f_user:dZptydDRnBXx2MA0QHJOfvznAeDK0orH@dpg-dblq2415efls73afdbn0-a/flask_hello_world_bv1f")
    curr = conn.cursor()
    curr.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        VALUES
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"

@app.route('/db_select')
def db_select():
    conn = psycopg2.connect("postgresql://flask_hello_world_bv1f_user:dZptydDRnBXx2MA0QHJOfvznAeDK0orH@dpg-dblq2415efls73afdbn0-a/flask_hello_world_bv1f")
    curr = conn.cursor()
    curr.execute('''
        SELECT * FROM Basketball;
        ''')
    records = curr.fetchall()
    conn.close()
    response_string = ""
    response_string += "<table>"
    for player in records:
        response_string += "<tr>"
        for info in player:
            response_string += f"<td>{info}</td>"
        response_string += "</tr>"
    response_string += "</table>"

    return response_string

@app.route('/db_drop')
def db_drop():
    conn = psycopg2.connect("postgresql://flask_hello_world_bv1f_user:dZptydDRnBXx2MA0QHJOfvznAeDK0orH@dpg-dblq2415efls73afdbn0-a/flask_hello_world_bv1f")
    curr = conn.cursor()
    curr.execute('''
        DROP TABLE Basketball;
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Dropped"