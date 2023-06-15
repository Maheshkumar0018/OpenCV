import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./images/pic1.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(gray,45,0.01,10)
# convert all corners in to int0
corners = np.int0(corners)

for i in corners:
    print("Co-ordinates X,Y: ",i)
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,(0,255,0),-1)

cv2.imshow('Shi_Tomasi',img)
if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows() 