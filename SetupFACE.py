import face_recognition
import pickle
# # Load a sample picture and learn how to recognize it.
# manh_image = face_recognition.load_image_file("./source/img_decode/manh.JPG")
# manh_face_encoding = face_recognition.face_encodings(manh_image)[0]

# # Load a second sample picture and learn how to recognize it.
# loan_image = face_recognition.load_image_file("./source/img_decode/loan.png")
# loan_face_encoding = face_recognition.face_encodings(loan_image)[0]

# atrung_image = face_recognition.load_image_file("./source/img_decode/atrung.jpg")
# atrung_face_encoding = face_recognition.face_encodings(atrung_image)[0]

all_face_encodings = {}

manh_image = face_recognition.load_image_file("./source/img_decode/manh.JPG")
all_face_encodings["manh"] = face_recognition.face_encodings(manh_image)[0]

loan_image = face_recognition.load_image_file("./source/img_decode/loan.png")
all_face_encodings["loan"] = face_recognition.face_encodings(loan_image)[0]

atrung_image = face_recognition.load_image_file("./source/img_decode/atrung.jpg")
all_face_encodings["atrung"] = face_recognition.face_encodings(atrung_image)[0]
# ... etc ...

with open('dataset_faces.dat', 'wb') as f:
    pickle.dump(all_face_encodings, f)