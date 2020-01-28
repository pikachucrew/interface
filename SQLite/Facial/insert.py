import sqlite3
from DataBase.data import User
 
conn = sqlite3.connect('../DataBase/db/test-table.db')

c = conn.cursor()

def insert_hour(hour):
    with conn:
        c.execute("INSERT INTO user_mood VALUES (?, ?, ?, ?, ?)", (hour.happy, hour.sad, hour.tired, hour.alert, hour.timestamp))

def get_hour_by_emotion(emotion, val):
    c.execute("SELECT * FROM user_mood WHERE %s = %d" % (emotion, val))
    return c.fetchall()

def remove_hour(hour):
    with conn:
        c.execute("DELETE from user_mood WHERE timestamp = :timestamp", {'timestamp': hour.timestamp})

hour_1 = User(15, 5, 10, 15, '12.48.32')
hour_2 = User(10, 5, 15, 10, '12.53.32')
hour_3 = User(5, 10, 15, 5, '12.58.32')

insert_hour(hour_1)
insert_hour(hour_2)
insert_hour(hour_3)

hours = get_hour_by_emotion('sad', 5)
print(hours)

conn.close()