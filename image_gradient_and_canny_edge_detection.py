import cv2
import matplotlib.pyplot as plt
import numpy as np

# Image gradient refers to the change in intensity or color values across an image. 
# It represents the spatial variations in pixel intensities and provides information about-
# the image's local changes and edges.

img = cv2.imread('./images/messi.jpg',cv2.IMREAD_GRAYSCALE)

# Laplacian filter:- second-order spatial derivatives of the image intensity values.
lap = cv2.Laplacian(img,cv2.CV_64F,ksize=3) # CV_64F : datatype 64 bit float, it supports negetive numbers
lap = np.uint8(np.absolute(lap))

# Sobel gradient representation: First-order spatial derivatives
sobelx = cv2.Sobel(img,cv2.CV_64F,dx=1,dy=0) #ksize=3
sobely = cv2.Sobel(img,cv2.CV_64F,dx=0,dy=1) #ksize=3

sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))

# sobelcombine
sobelComibe = cv2.bitwise_or(sobelx,sobely)

# Canny edge detection
canny = cv2.Canny(img,100,200,)

titles = ['Original','laplacian_filter','sobelx','sobely','sobelComibe','Canny']
images = [img,lap,sobelx,sobely,sobelComibe,canny]

for i in range(6):
    plt.subplot(3,3,i+1),plt.title(titles[i])
    plt.imshow(images[i],cmap='gray')
    plt.xticks([])
    plt.yticks([])
plt.show()