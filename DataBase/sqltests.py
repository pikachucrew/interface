import sqlite3
from data import User
import os

# os.getcwd() + 'DataBase/db/test-table.db'

conn = sqlite3.connect('db/test-table.db')

#creates the database in RAM, allowing for a fresh database to be created every time the file is run - useful for testing
# conn = sqlite3.connect(':memory:')

c = conn.cursor()

# c.execute("""CREATE TABLE user_emotions (
#     angry integer,
#     disgust integer,
#     fear integer,
#     happy integer,
#     sad integer,
#     surprise integer,
#     neutral integer,
#     timestamp text
# )""")


def insert_row():
    with conn:
        c.execute("INSERT INTO user_emotions VALUES (5, 10, 15, 20, 25, 30, 35, 'now')")

def get_rows():
    c.execute("SELECT * FROM user_emotions")
    return c.fetchall()


# insert_row()

#example of delete function
#def remove_hour(hour):
    #with conn:
       # c.execute("DELETE from user_mood WHERE timestamp = :timestamp", {'timestamp': hour.timestamp})
print(get_rows())



conn.close()
