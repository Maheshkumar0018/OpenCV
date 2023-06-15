
#  Background Subtractor using the Gaussian Mixture Models (MOG)
# additionally we install bgsegm - pip install opencv-contrib-python

import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture('./videos/vtest.avi')
# bgsegm: - Library
fgbg_MOG = cv2.bgsegm.createBackgroundSubtractorMOG()
fgbg_MOG2 = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
while(cap.isOpened()):
    _, frame = cap.read()
    if frame is None:
        break
    fgmask_MOG = fgbg_MOG.apply(frame)
    fgmask_MOG2 = fgbg_MOG2.apply(frame)
    cv2.imshow('Original_Frame',frame)
    cv2.imshow('fgmask_MOG',fgmask_MOG)
    cv2.imshow('fgmask_MOG2',fgmask_MOG2)
    key = cv2.waitKey(30)
    if key == ord('q') or key == 27:
        break
cap.release()
cv2.destroyAllWindows()
