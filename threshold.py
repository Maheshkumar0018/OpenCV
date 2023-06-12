import cv2
import numpy as np

# threshold use a global value to all pixels in a image 

img = cv2.imread('./images/building-windows.jpg',0)

_, th1 = cv2.threshold(img,150,255,cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img,150,255,cv2.THRESH_BINARY_INV) # inverse of threshold
_, th3 = cv2.threshold(img,180,255,cv2.THRESH_TRUNC) # if any pixels exceed a certain threshold is set to the maximum value, while pixel values below the threshold remain unchanged
_, th4 = cv2.threshold(img,180,255,cv2.THRESH_TOZERO) # if any pixel below the threshold is converted to Zero
_, th5 = cv2.threshold(img,180,255,cv2.THRESH_TOZERO_INV) # inverse of Thresh Zero

cv2.imshow('Original_image',img)
cv2.imshow('Threshold_image_1',th1)
cv2.imshow('Threshold_inverse_1',th2)
cv2.imshow('Threshold_ToZero',th4)
cv2.imshow('Threshold_ToZero_Inv',th5)
cv2.waitKey(0)

cv2.destroyAllWindows()