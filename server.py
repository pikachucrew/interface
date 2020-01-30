from flask import Flask
from flask import request
import json
import sqlite3
from flask_cors import CORS

server = Flask(__name__)
CORS(server)


@server.route('/<username>', methods = ['GET', 'POST'])
def facial(username):
    conn = sqlite3.connect('DataBase/test-table.db')
    c = conn.cursor()
    def get_rows():
        c.execute("SELECT * FROM user_emotions")
        return c.fetchall()
    def insert_rows(data):
        c.execute("INSERT INTO user_emotions VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
        (data['neutral'], data['happy'], data['sad'], data['angry'], data['fearful'], data['disgusted'], data['surprised'], data['timestamp']))
    if request.method == 'GET':
        return (json.dumps(get_rows()), 200)

    if request.method == 'POST':
        data = request.get_json()
        insert_rows(data)
        return "Data added"
    conn.close()


