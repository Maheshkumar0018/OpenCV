import cv2
import numpy as np



img1 = np.zeros((250,500,3),np.uint8)
img1 = cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
img2 = cv2.imread('./images/rectangle.jpg')

height, width, _ = img1.shape
img2 = cv2.resize(img2, (width, height))
#bitAnd = cv2.bitwise_and(img2,img1)
#bitOr = cv2.bitwise_or(img1,img2)
#bitXoo = cv2.bitwise_xor(img1,img2)  # T + T = F, F + F =F
bitNot = cv2.bitwise_not(img1,img2)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('bitAnd',bitNot)

cv2.waitKey(0)
cv2.destroyAllWindows()