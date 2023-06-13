import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('./images/opencv.png')
imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(imggray,127,255,0)
contours,hirarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE) # hirarchy: contain info about img topology
print("Number of Contours = "+str(len(contours)))

cv2.drawContours(img,contours,-1,(0,255,0),3)

cv2.imshow('Original image',img)
cv2.imshow('Gray image',imggray)

cv2.waitKey(0)

cv2.destroyAllWindows()