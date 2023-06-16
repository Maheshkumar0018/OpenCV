import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture('./videos/traffic-mini.mp4')
_,frame = cap.read()
x,y,width,height = 130,100,330,1400
track_window = (x,y,width,height)
roi = frame[y:y+height,x:x+width]
# cvt roi to HSV
hsv_roi = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi,np.array((0.,60.,32.)),np.array((180.,255.,255)))

roi_hst = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180]) # hue channel

cv2.normalize(roi_hst,roi_hst,0,255,cv2.NORM_MINMAX) 
term_crit = (cv2.TermCriteria_EPS | cv2.TERM_CRITERIA_COUNT ,10,1)
while(cap.isOpened()):
    _,frame = cap.read()
    if _ == True:
        # cal hsv roi val
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv],[0],roi_hst,[0,180],1) # backprojected
        ret,track_window = cv2.CamShift(dst,track_window,term_crit)
        #x,y,w,h = track_window
        #final_img = cv2.rectangle(frame,(x,y),(x+w,y+h),255,3)
        pts = cv2.boxPoints(ret)
        print("PTS",pts)
        pts = np.int0(pts)
        final_img = cv2.polylines(frame,[pts],True,(0,255,0),thickness=2)
        cv2.imshow('Frame',final_img)
        cv2.imshow('BackProject_Frame',dst)
        k = cv2.waitKey(30) & 0xFF
        if k == 27 or k == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()