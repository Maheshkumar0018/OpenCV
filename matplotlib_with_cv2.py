import cv2 
import numpy as np
import matplotlib.pyplot as plt


#img = cv2.imread('./images/messi.jpg')
#cv2.imshow('img',img)

#img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#plt.imshow(img)
#plt.xticks([]);plt.yticks([])
#plt.show()

img = cv2.imread('./images/building-windows.jpg',0)

_, th1 = cv2.threshold(img,150,255,cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img,150,255,cv2.THRESH_BINARY_INV) # inverse of threshold
_, th3 = cv2.threshold(img,180,255,cv2.THRESH_TRUNC) # if any pixels exceed a certain threshold is set to the maximum value, while pixel values below the threshold remain unchanged
_, th4 = cv2.threshold(img,180,255,cv2.THRESH_TOZERO) # if any pixel below the threshold is converted to Zero
_, th5 = cv2.threshold(img,180,255,cv2.THRESH_TOZERO_INV) # inverse of Thresh Zero

titles = ['Original Img','Binary','Binary_Inv','Thresh_Trunc','Thresh_ToZero','Thresh_ToZero_Inv']
images = [img,th1,th2,th3,th4,th5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],cmap='gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
