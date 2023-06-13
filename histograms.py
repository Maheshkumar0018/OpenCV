import cv2
import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((200,200),np.uint8)

cv2.imshow('image',img)
cv2.waitKey(0)

cv2.destroyAllWindows()