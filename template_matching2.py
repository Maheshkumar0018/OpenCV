import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./images/chicky_512.png')
template = cv2.imread('./images/chicky_mouth.png')

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)

w,h = template_gray.shape[::-1]

res = cv2.matchTemplate(img_gray,template_gray,cv2.TM_CCOEFF_NORMED)
print('res: ',res)

threshold = 0.9
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    print("pt:",pt)
    cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,0,255),2)


cv2.imshow('img',img)
cv2.imshow('template',template)
cv2.waitKey(0)
cv2.destroyAllWindows()