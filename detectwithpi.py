# import picamera
# import  pyshine as ps #  pip3 install pyshine==0.0.9
import numpy as np
import os
import pickle, sqlite3
import cv2
# from PIL import Image
#--------------------------------------------------------------------
# CODE KET NOI DU LIEU NHAN DIEN HINH ANH KHUON MAT
HTML="""
<html>
<head>
<title>PyShine Live Streaming</title>
</head>

<body>
<center><h1> PyShine Live Streaming using PiCamera </h1></center>
<center><img src="stream.mjpg" width='640' height='480' autoplay playsinline></center>
</body>
</html>
"""
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
# def get_picamera():
#     StreamProps = ps.StreamProps
#     StreamProps.set_Page(StreamProps,HTML)
#     address = ('192.168.1.1',9000) # Enter your IP address 
#     StreamProps.set_Mode(StreamProps,'picamera')    
#     with picamera.PiCamera(resolution='640x480', framerate=30) as camera:
#         output = ps.StreamOut()
#         StreamProps.set_Output(StreamProps,output)
#         camera.rotation = 90
#         camera.start_recording(output, format='mjpeg')
#         try:
#             server = ps.Streamer(address, StreamProps)
#             print('Server started at','http://'+address[0]+':'+str(address[1]))
#             server.serve_forever()
#         finally:
#             camera.stop_recording()
# cap = cv2.VideoCapture("http://169.254.21.65:9000")
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_COMPLEX
while True:

    ret, img = cap.read()
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
                cv2.putText(img, ""+str(profile[1]), (x+10, y), font, 1, (0,255,0), 1)
                print("Xin chao Anh/Chi " + str(profile[1]) + "toi MAJ")
        else:
            cv2.putText(img, "Unknown", (x, y + h + 30), font, 0.4, (0, 0, 255), 1)


    cv2.imshow('img', img)
    if(cv2.waitKey(1) == ord('q')):
        break
cap.release()
cv2.destroyAllWindows()

