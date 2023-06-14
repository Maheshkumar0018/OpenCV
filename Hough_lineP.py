# HoughlinesP: is an optimization of Houghlines
# intead of taking all points into consideration, it will take random subset of point swhich is sufficient for line Detection

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('./images/road1.jpg')
gray_img =  cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray_img,50,255,apertureSize=3) # thrshold 50 max 150
cv2.imshow('Canny_Edhe',edges)
# maxLineGap: maximum allowed gap between line segments to treat them as single line
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
# HoughlinesP: will directly give/return the two points ie, (x1,y1),(x2,y2)
# but in Normal HoughLines will return distance(rho),theta.
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow('HoughlinesP',img)
cv2.waitKey(0)
cv2.destroyAllWindows()