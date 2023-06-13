import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('./images/ml.png')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
template = cv2.imread('./images/ml_face.png')
template_gray = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
w,h = template_gray.shape[::-1]
result = cv2.matchTemplate(img_gray,template_gray,cv2.TM_CCOEFF_NORMED) # img,template,method

print(result)
threshold = 0.9
loc = np.where(result >= threshold)
print("loc",loc)

for pt in zip(*loc[::-1]):
    print("pt:",pt)
    cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,0,255),2)


cv2.imshow('image',img)
cv2.imshow('template',template)
cv2.waitKey(0)

cv2.destroyAllWindows()