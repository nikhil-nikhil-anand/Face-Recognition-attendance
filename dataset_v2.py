import cv2
import numpy as np
import os
import time
import random


cap = cv2.VideoCapture(0)
count = 0
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


name=input("Enter your name: ")
if not os.path.exists("Dataset/train/" + name):
    os.mkdir("Datasets/train/" + name)
else:
    print("Directory already exists")

if not os.path.exists("Datasets/test/" + name):
    os.mkdir("Datasets/test/" + name)
else:
    print("Directory already exists")


def face_extractor(frame,count):
    n=0
    faces = face_classifier.detectMultiScale(frame, 1.3, 5)
    if faces == ():
        return None
    for (x,y,w,h) in faces:
        x=x-10
        y=y-10
        cropped_face = frame[y-40:y+h+50, x-40:x+w+50]

    if count%8==0:
        return cropped_face
    elif count%8==1:
        return cropped_face
    elif count%8==2:
        return cropped_face
    elif count%8==3:
        alpha = random.uniform(0.5, 1.1)
        beta = random.randint(0,15)
        cropped_face = cv2.convertScaleAbs(cropped_face, alpha=alpha, beta=beta)
        return cropped_face
    elif count%8==4:
        x1=random.randint(0,4)
        x2=random.randint(212,224)
        y1=random.randint(0,4)
        y2=random.randint(212,224)
        cropped_face= cropped_face[x1:x2,y1:y2]
        return cropped_face
    elif count%8==5:
        cropped_face = cv2.GaussianBlur(cropped_face, (11, 11), 0)
        return cropped_face
    elif count%8==6:
        cropped_face = cv2.bilateralFilter(cropped_face, 9, 75, 75)
        return cropped_face
    elif count%8==7:
        alpha = random.uniform(0.6, 1.2)
        beta = random.randint(3,20)
        cropped_face = cv2.convertScaleAbs(cropped_face, alpha=alpha, beta=beta)
        return cropped_face


cap = cv2.VideoCapture(0)
count = 0
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:

    ret, frame = cap.read()
    if face_extractor(frame,count) is not None:
        count += 1
        face = cv2.resize(face_extractor(frame,count), (224, 224))
        if count <= 150:
            cv2.imwrite("Datasets/train/" + name + "/" + str(count) + ".jpg", face)
        else:
            cv2.imwrite("Datasets/test/" + name + "/" + str(count) + ".jpg", face)
        cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
        cv2.imshow('Face Cropper', face)
        #time.sleep(0.01)
        if count >= 200:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
cap.release()
cv2.destroyAllWindows()      
print("Collecting Samples Complete")