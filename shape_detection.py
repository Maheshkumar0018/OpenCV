import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./images/shapes2.png')
imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,threshold = cv2.threshold(imggray,240,255,cv2.THRESH_BINARY)
contours,_ = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
for contour in contours:
    approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True) # cureve, Epsilon, arcLength, closed or not
    cv2.drawContours(img,[approx],0,(0,0,0),5) # 0: contour indx
    x = approx.ravel()[0] 
    y = approx.ravel()[1] -5
    if len(approx) == 3:
        cv2.putText(img,'Triangle',(x,y),cv2.FONT_HERSHEY_COMPLEX,.5,(0,0,0))
    elif len(approx) == 4:
        x,y,w,h = cv2.boundingRect(approx)
        aspectratio = float(w)/h
        print('Aspectratio: ',aspectratio)
        if aspectratio >= 0.95 and aspectratio <= 1.05:
            cv2.putText(img,'Square',(x,y),cv2.FONT_HERSHEY_COMPLEX,.5,(0,0,0))
        else:
            cv2.putText(img,'Rectangle',(x,y),cv2.FONT_HERSHEY_COMPLEX,.5,(0,0,0))
    elif len(approx) == 5:
        cv2.putText(img,'Pentagon',(x,y),cv2.FONT_HERSHEY_COMPLEX,.5,(0,0,0))
    elif len(approx) == 10:
        cv2.putText(img,'Star',(x,y),cv2.FONT_HERSHEY_COMPLEX,.5,(0,0,0))
    elif len(approx) == 1:
        cv2.putText(img,'Heart',(x,y),cv2.FONT_HERSHEY_COMPLEX,.5,(0,0,0))
    elif len(approx) == 2:
        cv2.putText(img, 'Half Heart', (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

    else:
        cv2.putText(img,'Circle',(x,y),cv2.FONT_HERSHEY_COMPLEX,.5,(0,0,0))



#cv2.imshow('image',imggray)
cv2.imshow('Original_image',img)
plt.show()
cv2.waitKey(0)

cv2.destroyAllWindows()