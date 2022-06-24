# main
# img -> encode (128 bit) -> histogram extract -> output(id)
import numpy as np
import sqlite3
import cv2
import face_recognition
import csv 
from source.caltime import caltime_arrive
face_cascade = cv2.CascadeClassifier('./source/haarcascade_frontalface_alt.xml')
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
def rotate(input, n):
    return input[n:] + input[:n]  
id_staff = 0
def process_staff(staff):
    global id_staff
    for i in range(0, len(staff)):
        id_staff += 1
        staff[i].append(id_staff)
        staff[i] = rotate(staff[i], -1)  
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_COMPLEX
# Load a sample picture and learn how to recognize it.
manh_image = face_recognition.load_image_file("./source/img_decode/manh.JPG")
manh_face_encoding = face_recognition.face_encodings(manh_image)[0]

# Load a second sample picture and learn how to recognize it.
loan_image = face_recognition.load_image_file("./source/img_decode/loan.png")
loan_face_encoding = face_recognition.face_encodings(loan_image)[0]

atrung_image = face_recognition.load_image_file("./source/img_decode/atrung.jpg")
atrung_face_encoding = face_recognition.face_encodings(atrung_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    manh_face_encoding,
    loan_face_encoding,
    atrung_face_encoding
]
print("manh: ", manh_face_encoding)
print("loan: ", loan_face_encoding)
print("atrung: ", atrung_face_encoding)
print("encode: ", known_face_encodings)
known_face_names = [
    "manh",
    "loan",
    "atrung"
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
detect_face_histogram = "his"
detect_face_encode = "enc"

staff_before = []

while True:
    ret, img = cap.read()
    frame = img
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        # cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        nbr_predicted, conf = recognizer.predict(gray[y:y+h, x:x+w])
        if conf < 90:
            profile=getProfile(nbr_predicted)
            if profile != None:
                detect_face_histogram = str(profile[1])
                print("Histogram done")
                # print("Xin chao Anh/Chi " + str(profile[1]) + " toi MAJ")
        else:
            cv2.putText(img, "Unknown", (x, y + h + 30), font, 0.4, (0, 0, 255), 1)

    # Only process every other frame of video to save time
    if process_this_frame:
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]
        
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        detect_face_encode = str(name)
        print("Encode done")
    if detect_face_histogram == detect_face_encode:
        print("Xin chao " + str(name).upper() + " toi MAJ")
        staff = caltime_arrive(str(name))
        # process_staff(staff)
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        detect_face_histogram = "his"
        detect_face_encode = "enc"
    cv2.imshow('MAJ Vision', img)
    if(cv2.waitKey(1) == ord('q')):
        break
cap.release()
cv2.destroyAllWindows()
