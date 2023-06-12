import cv2
import numpy as np

# Adaptive threshold calculate threshold for smaller region of image 

img = cv2.imread('./images/Piano_Sheet_Music.png',0)

_, th1 = cv2.threshold(img,90,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,7) # Thresh avl is mean the of neibhourhood area
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,7)

cv2.imshow('Original_image',img)
#cv2.imshow('Threshold_image_1',th1)
cv2.imshow('Adaptive_Threshold_mean_c',th2)
cv2.imshow('Adaptive_Threshold_Gaussian_c',th3)
cv2.waitKey(0)

cv2.destroyAllWindows()