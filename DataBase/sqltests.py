import sqlite3
from data import User
import os

# os.getcwd() + 'DataBase/db/test-table.db'

conn = sqlite3.connect(os.getcwd() + '/DataBase/db/test-table.db')

#creates the database in RAM, allowing for a fresh database to be created every time the file is run - useful for testing
# conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE user_emotions (
    angry integer,
    disgust integer,
    fear integer,
    happy integer,
    sad integer,
    surprise integer,
    neutral integer,
    timestamp text
)""")


def insert_row(row):
    with conn:
        c.execute("INSERT INTO user_emotions VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                  (row.emotions.angry, row.emotions.disgust, row.emotions.fear, row.emotions.happy, row.emotions.sad, row.emotions.surprise, row.emotions.neutral, row.timestamp))

def get_rows():
    c.execute("SELECT * FROM user_mood")
    return c.fetchall()

#example of delete function
#def remove_hour(hour):
    #with conn:
       # c.execute("DELETE from user_mood WHERE timestamp = :timestamp", {'timestamp': hour.timestamp})




conn.close()
