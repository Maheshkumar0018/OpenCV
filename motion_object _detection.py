import cv2
import matplotlib.pyplot as plt
import numpy as np

cap = cv2.VideoCapture('./videos/tree.avi')
_,frame1 = cap.read()
_,frame2 = cap.read()

while cap.isOpened():
    diff  = cv2.absdiff(frame1,frame2) # helps to highlight the regions where motion has occurred
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY) 
    blur = cv2.GaussianBlur(gray,(5,5),0) # reduce noise, smooth out variations
    _, thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh,None,3) # kernal-none, noof iterations-3
    contours,_ = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # print("Countou:", contour)
        (x,y,w,h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) < 700:
            continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        

    #cv2.drawContours(frame1,contours,-1,(0,255,0),2)

    cv2.imshow("inter",frame1)
    # need to compare the current frame (frame2) with the subsequent - 
    # frame to continue the motion detection or tracking process.
    #  you ensure that the previous frame remains updated with the latest frame
    frame1 = frame2
    _,frame2 = cap.read()
    if cv2.waitKey(40) == 27:
        break
cv2.destroyAllWindows()
cap.release()