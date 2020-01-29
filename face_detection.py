import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
import json
from fer import FER
import tensorflow as tf
import time 
import sqlite3


def insert_row(row):
    with conn:
        c.execute("INSERT INTO user_emotions VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                  (row["emotions"]["angry"], row["emotions"]["disgust"], row["emotions"]["fear"], row["emotions"]["happy"], row["emotions"]["sad"], row["emotions"]["surprise"], row["emotions"]["neutral"], row["timestamp"]))


def get_rows():
    c.execute("SELECT * FROM user_emotions")
    return c.fetchall()

tf.ConfigProto = tf.compat.v1.ConfigProto
tf.Session = tf.compat.v1.Session

detector = FER()

def detect_faces():
  while True:
    conn = sqlite3.connect(os.getcwd() + '/DataBase/db/test-table.db')
    c = conn.cursor()
    webcam = cv2.VideoCapture(0)
    check, frame = webcam.read()
    print(check)
    cv2.imwrite('captured_img.jpg', frame)
    webcam.release()
    # assigns image to variable img
    img = cv2.imread('captured_img.jpg')

    img_copy = img.copy()

    #converts img to grayscale
    img_gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)

    #function that should convert back into colour when invoked, isn't currently working
    def convertToRGB(image):
      return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    #assigns the classifier (which is the instructions of what to look for in img) to a variable
    haar_cascade_face = cv2.CascadeClassifier(
        os.getcwd() + '/data/haarcascade_frontalface_default.xml')

    #invokes cascade on img
    faces_rects = haar_cascade_face.detectMultiScale(img_gray, scaleFactor=1.2, minNeighbors=5)

    #prints number of faces found to console
    print('Faces found: ', len(faces_rects))

    #draws rectangle around face
    for (x,y,w,h) in faces_rects:
      cv2.rectangle(img_copy, (x, y), (x+w, y+h), (0, 255, 0), 2)

    detector_output = detector.detect_emotions(img_copy)
    


    if len(faces_rects) > 0:
      for emotion in detector_output[0]["emotions"]:
      detector_output[0]["emotions"][emotion] = int(detector_output[0]["emotions"][emotion].item() * 100)
      output_dict = {"emotions": detector_output[0]["emotions"], "timestamp": time.ctime(time.time())}
    else: 
      output_dict = {"emotions": {"angry": 0, 'disgust': 0, 'fear': 0,
                                  'happy': 0, 'sad': 0, 'surprise': 0, 'neutral': 0}, "timestamp": time.ctime(time.time())}


    #print(output_dict["emotions"])
    insert_row(output_dict)

    #if len(faces_rects) > 0:
      #output_dict["face_present"] = True
      #output_dict["emotions"] = str(detector_output[0]["emotions"])

    #json_string = json.dumps(output_dict)

    #with open('json_file.json', 'w') as f:
      #json.dump(output_dict, f)

    print(get_rows())
    conn.close()

    time.sleep(5.0)








#displays img
# plt.imshow(convertToRGB(img_copy))
# plt.show()
