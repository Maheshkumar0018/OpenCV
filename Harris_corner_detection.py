# This function measures the similarity between the intensity pattern around the pixel and a shifted version 
#of itself. By comparing the intensity variations in different directions, the algorithm can identify regions 
#with significant changes in intensity, which are likely to correspond to corners.

import cv2
import  numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./images/pic1.png')
desired_width = 800
desired_height = 600
img = cv2.resize(img, (desired_width, desired_height))

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_img = np.float32(gray_img)
dst = cv2.cornerHarris(gray_img,2,3,0.04) #img,blocksize(window),k-size,k:-sensitivity of the corner detection.
dailate = cv2.dilate(dst,None)
print("dst: ",dst)
print("len: ",str(len(img[dst > 0.01 * dst.max()])))
# reverting back to original img
img[dst > 0.01 * dst.max()] = [0,255,0]
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()