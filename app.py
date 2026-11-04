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