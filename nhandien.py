import numpy as np
import os
import pickle, sqlite3
import cv2
from PIL import Image
import time
#--------------------------------------------------------------------
# CODE KET NOI DU LIEU NHAN DIEN HINH ANH KHUON MAT

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read("recognizer/trainningData.yml")

def getProfile(Id):
    conn=sqlite3.connect("FaceBase.db")
    query="SELECT * FROM people WHERE ID="+str(Id)
    cursor=conn.execute(query)
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile

start_time = time.time()
img = cv2.imread("phuong.jpg")
font = cv2.FONT_HERSHEY_COMPLEX
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        nbr_predicted, conf = recognizer.predict(gray[y:y+h, x:x+w])
        if conf < 70:
            profile=getProfile(nbr_predicted)
            if profile != None:
                cv2.putText(img, ""+str(profile[1]), (x+10, y), font, 1, (0,255,0), 1);
        else:
            cv2.putText(img, "Unknown", (x, y + h + 30), font, 0.4, (0, 0, 255), 1);

cv2.imshow('img', img)
print("--- %s seconds ---" % (time.time() - start_time))

cv2.waitKey(0)
cv2.destroyAllWindows()

