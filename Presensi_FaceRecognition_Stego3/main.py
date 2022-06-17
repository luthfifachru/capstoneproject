#Capstone Project Kelompok 3 Stego 2022
#Luthfi Fachruddin
#Khairunnisa
#Muhammad Ariyadi
#Keyrien Liana
#Jesita Dosma

import os
from datetime import datetime
import cv2
import numpy as np


import azuredatabase

import face_recognition 

#Tetapkan lokasi folder dan buat daftar gambar.
path = 'Wajah_yang_dikenali'
images = []
personNames = []
myList = os.listdir(path)

#Membaca list face
for cu_img in myList:
    current_Img = cv2.imread(f'{path}/{cu_img}')
    images.append(current_Img)
    personNames.append(os.path.splitext(cu_img)[0])
print(personNames)

#fungsi untuk encode image
def faceEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

#memanggil program azuredatabase.py dan create data
azuredatabase.create_data()

#fungsi untuk mengecek gambar dari kamera dan melakukan perbandingan terhadap gambar yang ada
def check_name_state(name):
    now = datetime.now()
    d1 = now.strftime("%H:%M:%S")
    if (not azuredatabase.exist_name(name,d1)):
        dtstring = now.strftime("%d/%m/%Y %H:%M:%S")
        azuredatabase.insert_data(name, dtstring)

encodeListKnown = faceEncodings(images)
print('All Encodings Complete!!!')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    faces = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
    faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

    facesCurrentFrame = face_recognition.face_locations(faces)
    encodesCurrentFrame = face_recognition.face_encodings(faces, facesCurrentFrame)

    for encodeFace, faceLoc in zip(encodesCurrentFrame, facesCurrentFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        # print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = personNames[matchIndex].upper()
            print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            # MarkAttendance(name)
            check_name_state(name)

    cv2.imshow('Webcam', frame)
    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()













