import cv2
import numpy as np
import os
import time
import random


cap = cv2.VideoCapture(0)
count = 0
prev_frame_time = 0
new_frame_time = 0
while True:
    ret, frame = cap.read()
    #frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    font = cv2.FONT_HERSHEY_SIMPLEX
    new_frame_time = time.time()
    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time
    fps = int(fps)
    cv2.putText(frame, str(fps), (7, 70), font, 3, (0, 0, 0), 3, cv2.LINE_AA)

    cv2.imshow('Face Cropper', frame)
    if count >= 200:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()      
print("Collecting Samples Complete")