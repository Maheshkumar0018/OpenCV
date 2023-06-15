import cv2
import numpy as np

cap = cv2.VideoCapture('./videos/vtest.avi')
#fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()
fgbg = cv2.createBackgroundSubtractorKNN()
kernal = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
while(cap.isOpened()):
    _,frame = cap.read()
    if frame is None:
        break
    fg_mask = fgbg.apply(frame)
    fg_mask = cv2.morphologyEx(fg_mask,cv2.MORPH_OPEN,kernal)
    cv2.imshow('Frame',frame)
    cv2.imshow('KNN_Frame',fg_mask)
    #cv2.imshow('GMH_Frame',fg_mask)
    key = cv2.waitKey(30)
    if key == ord('q') or key == 27:
        break
cap.release()
cv2.destroyAllWindows()