import cv2
import numpy as np
import os

modelFile = "res10_300x300_ssd_iter_140000.caffemodel"
configFile = "deploy.prototxt.txt"

net = cv2.dnn.readNetFromCaffe(configFile, modelFile)

name=input("Enter your name: ")
if not os.path.exists("Dataset/train/" + name):
    os.mkdir("Datasets/train/" + name)
else:
    print("Directory already exists")

if not os.path.exists("Datasets/test/" + name):
    os.mkdir("Datasets/test/" + name)
else:
    print("Directory already exists")


cap = cv2.VideoCapture(0)
prev_frame_time = 0
new_frame_time = 0
count= 0

while True:
    
    ret, frame = cap.read()
    h, w = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,(300, 300), (104.0, 117.0, 123.0))
    net.setInput(blob)
    faces = net.forward()
    for i in range(faces.shape[2]):
            confidence = faces[0, 0, i, 2]
            if confidence > 0.5:
                box = faces[0, 0, i, 3:7] * np.array([w, h, w, h])
                (x, y, x1, y1) = box.astype("int")
                cv2.rectangle(frame, (x, y), (x1, y1), (0, 0, 255), 2)

    #cv2.imshow('Face Cropper', frame)
    face = cv2.resize(frame, (224, 224))
    if count <= 150:
        cv2.imwrite("Datasets/train/" + name + "/" + str(count) + ".jpg", face)
    else:
        cv2.imwrite("Datasets/test/" + name + "/" + str(count) + ".jpg", face)
    cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
    cv2.imshow('Face Cropper', face)
    if count >= 200:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()  


