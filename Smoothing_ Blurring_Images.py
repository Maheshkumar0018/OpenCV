import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('./images/lena.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


# homegeneous filter: where each element in the filter kernel has the same value 
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)

# One-dimensional signals:- There is only one signal with different values along its length.  
# One-dimensional signals can also filtered with Low-pass filters (LPF), and High-pass-filters (HPF).
# Low-pass-filters: removing noise, blurring images
# High-pass-filters: finding edges 

# blur
blur = cv2.blur(img,(5,5))

# Gaussian Filter:- use a different weight in x,y
gblur = cv2.GaussianBlur(img,(5,5),0)

# median filter
median = cv2.medianBlur(img,5) # kernal size must be odd except odd

#  bilateral filter is a non-linear filter used for image smoothing while preserving edges. 
# bilateral filter considers both the spatial distance between pixels and the intensity difference between pixels.
bilateral_filter = cv2.bilateralFilter(img,9,75,75)



images = [img,dst,blur,gblur,median,bilateral_filter]
titles = ['Original','homegeneous filter','Blur','Gaussian Blur','Median','Bilateral filetr']

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],cmap='gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

cv2.destroyAllWindows()
plt.imshow(img)
plt.show()