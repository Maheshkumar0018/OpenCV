import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./images/checkerboard_color.png',cv2.IMREAD_COLOR)
print(img)
print("shape of Img: ",img.shape)

img = cv2.line(img,(0,0),(255,244),(255,0,0),5)
img = cv2.arrowedLine(img,(0,0),(0,255),(255,0,0),5)
cv2.imshow('window',img)
key = cv2.waitKey(0)



