import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('./images/smarties.png',cv2.IMREAD_GRAYSCALE)
_,mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)

kernal = np.ones((5,5),np.uint8)
# dailation 
dailation = cv2.dilate(mask,kernal,iterations=2)

# Erosion: removes pixels from the edges and shrinks the shapes.
erosion = cv2.erode(mask,kernal,iterations=1)

# Opening: Erosion followed by dailation
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)

# Closing: dailation follwed by Erosion
closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal)

# Morph_Gradient: diff b/w dailation and erosion of an img
MG = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernal)

# TopHat: diff between img and opening of an img
th = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernal)

titles = ['image','mask','dailation','erosin','opening','closing','Morph_Gradient','TopHat']
images = [img,mask,dailation,erosion,opening,closing,MG,th]

for i in range(8):
    plt.subplot(2,4,i+1),plt.imshow(images[i],cmap='gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()