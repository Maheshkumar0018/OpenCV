import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread('./images/lena.jpg',cv2.IMREAD_GRAYSCALE)

# Canny edge detection
canny = cv2.Canny(img,100,200,)

titles = ['Original','Canny']
images = [img,canny]

for i in range(2):
    plt.subplot(1,2,i+1),plt.title(titles[i])
    plt.imshow(images[i],cmap='gray')
    plt.xticks([]),plt.yticks([])

plt.show()