import cv2
import numpy as np
import matplotlib.pyplot as plt

# use default pre-trained CascadeClassifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def detect(gray,frame):
    faces = face_cascade.detectMultiScale(gary,1.3,5)
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+w),(255,0,0),3)
        roi_gary = gary[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gary,1.1,3)
        for ex,ey,ew,eh in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
    return frame

video_captured = cv2.VideoCapture(0)
while(video_captured.isOpened()):
    _, frame = video_captured.read()
    gary = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    canvas = detect(gary,frame)
    cv2.imshow('Video',canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_captured.release()
cv2.destroyAllWindows()


