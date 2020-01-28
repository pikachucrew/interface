import sqlite3
from data import User
 
conn = sqlite3.connect('./db/test-table.db')

#creates the database in RAM, allowing for a fresh database to be created every time the file is run - useful for testing
# conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE user_mood (
    happy integer,
    sad integer,
    tired integer,
    alert integer,
    timestamp text
)""")

def insert_hour(hour):
    with conn:
        c.execute("INSERT INTO user_mood VALUES (?, ?, ?, ?, ?)", (hour.happy, hour.sad, hour.tired, hour.alert, hour.timestamp))

def get_hour_by_emotion(emotion, val):
    c.execute("SELECT * FROM user_mood WHERE %s = %d" % (emotion, val))
    return c.fetchall()

# #example of update function
# def update_emotion(emotion, updated_val, hour):
#     with conn:
#         c.execute("UPDATE user_mood SET %s = %d WHERE timestamp = %s" % (emotion, updated_val, hour.timestamp))

#example of delete function
def remove_hour(hour):
    with conn:
        c.execute("DELETE from user_mood WHERE timestamp = :timestamp", {'timestamp': hour.timestamp})

hour_1 = User(15, 5, 10, 15, '12.28.32')
hour_2 = User(10, 5, 15, 10, '12.33.32')
hour_3 = User(5, 10, 15, 5, '12.38.32')

insert_hour(hour_1)
insert_hour(hour_2)
insert_hour(hour_3)

hours = get_hour_by_emotion('sad', 5)
print(hours)

# update_emotion('happy', 10, hour_1)
remove_hour(hour_2)
hours = get_hour_by_emotion('sad', 5)
print(hours)


conn.close()