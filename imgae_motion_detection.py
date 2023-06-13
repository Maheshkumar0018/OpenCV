import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./images/text_motion.jpg')



cv2.imshow('original',img)
cv2.waitKey(0)

cv2.destroyAllWindows()