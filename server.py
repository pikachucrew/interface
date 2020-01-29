from flask import Flask
from flask import request
from new_face import detect_face
import os
import json
import sqlite3

server = Flask(__name__)



@server.route('/<username>', methods = ['GET', 'POST'])
def facial(username):
    conn = sqlite3.connect(os.getcwd() + '/DataBase/db/test-table.db')
    c = conn.cursor()
    def get_rows():
        c.execute("SELECT * FROM user_emotions")
        return c.fetchall()
    def insert_rows(data):
        c.execute("INSERT INTO user_emotions VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
        (data['angry'], data['disgust'], data['fear'], data['happy'], data['sad'], data['surprise'], data['neutral'], data['timestamp']))
    if request.method == 'GET':
        return (json.dumps(get_rows()), 200)

    if request.method == 'POST':
        data = json.dumps(request.get_json())
        detect_face(data)
        return "Data added"
    conn.close()


