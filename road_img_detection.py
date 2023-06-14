import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('./images/road1.jpg')
print('image_shape: ',img.shape)
height = img.shape[0]
width = img.shape[1]
# ROI
region_of_Interest_vertices = [
    (0,height),
    (width/2,height/2),
    (width,height)
]

def region_of_interest(img,vertices):
    mask = np.zeros_like(img)


plt.imshow(img[:,:,::-1])
plt.show()
cv2.destroyAllWindows()