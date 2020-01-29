from fer.fer import FER
import cv2
import sqlite3
import time
import os



def detect_face(data):
  detector = FER()
  conn = sqlite3.connect('/DataBase/db/test-table.db')
  c = conn.cursor()

  def insert_row(row):
    with conn:
      c.execute("INSERT INTO user_emotions VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (row["emotions"]["angry"],
                 row["emotions"]["disgust"],
                    row["emotions"]["fear"],
                    row["emotions"]["happy"],
                    row["emotions"]["sad"],
                    row["emotions"]["surprise"],
                    row["emotions"]["neutral"],
                    row["timestamp"]))

  def get_rows():
    c.execute("SELECT * FROM user_emotions")
    return c.fetchall()

  decoded_img = base64.b64decode(data)
  filename = 'decoded_img.jpg'
  with open(filename, 'wb') as f:
    f.write(decoded_img)
  
  img = cv2.imread('decoded_img.jpg')
  img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  detector_output = detector.detect_emotions(img_gray)

  if len(detector_output) > 0:
    for emotion in detector_output[0]["emotions"]:
      detector_output[0]["emotions"][emotion] = int(
          detector_output[0]["emotions"][emotion].item() * 100)
      output_dict = {
          "emotions": detector_output[0]["emotions"], "timestamp": time.ctime(time.time())}
  else:
    output_dict = {"emotions": {"angry": 0, 'disgust': 0, 'fear': 0,
                                'happy': 0, 'sad': 0, 'surprise': 0, 'neutral': 0}, "timestamp": time.ctime(time.time())}

  insert_row(output_dict)
  print(get_rows())
  conn.close()
  os.remove('decoded_img.jpg')
