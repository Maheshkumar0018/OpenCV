import cv2
import matplotlib.pyplot as plt
import numpy as np
# HoughLines: ifinite lines
img = cv2.imread('./images/sudoku.png')
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# apertureSize:- parameter determines the size of the neighborhood considered when calculating the gradient of the image
edges = cv2.Canny(gray_img,50,150,apertureSize=3) # threshold 50 max 150
cv2.imshow("Canny_Edge",edges)
# ρ = x * cos(θ) + y * sin(θ)
#rho: The resolution parameter in pixels of the Hough accumulator. It determines the distance resolution of the detected lines.
lines = cv2.HoughLines(edges,1,np.pi/180,200)

for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho # is give the origin
    y0 = b*rho # is give the origin 
    # p(rho),theta we need to convert them into  Cartesian coordinates to To visualize the detected lines.
    # 1000 is used as an arbitrary scale factor. 
    # It determines the length of the line segment that will be drawn to represent the detected line.
    x1 = int(x0+1000*(-b))
    y1 = int(y0+1000*a)
    x2 = int(x0-1000*(-b))
    y2 = int(y0-1000*a)
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

    print("a:",a)
    print("b:",b)
    print("x0:",x0)
    print("y0:",y0)
    print("x1: ",x1)
    print("y1: ",y1)
    print("x2: ",x2)
    print("y2: ",y2)
    
cv2.imshow('Hough_transform:',img)
cv2.waitKey(0)
cv2.destroyAllWindows()