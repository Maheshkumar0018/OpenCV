import cv2
import matplotlib.pyplot as plt
import numpy as np

# Gaussian Pyramid: repeat filtering and sub sampling an image
# pyrDown reduce resolution of an img
# pyrUp increase resolution of an img

img = cv2.imread('./images/lena.jpg')
layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i),layer)

layer = gp[5]
cv2.imshow('upper level Gaussian pyramid:',layer)
lp = [layer]

for i in range(5,0,-1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1],gaussian_extended)
    #cv2.imshow(str(i),laplacian)



key = cv2.waitKey(0)
cv2.destroyAllWindows()