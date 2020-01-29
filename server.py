from flask import Flask
from flask import request
import detect_faces from face_detection
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
        detect_faces()
        # print(request.get_json())
        # data = request.get_json()
        # insert_rows(data)
        # conn.commit()
        # return (json.dumps(get_rows()), 200)
    conn.close()

