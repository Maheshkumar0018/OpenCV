import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("Track")

cv2.createTrackbar("LH","Track",0,255,nothing)
cv2.createTrackbar("LS","Track",0,255,nothing)
cv2.createTrackbar("LV","Track",0,255,nothing)

cv2.createTrackbar("UH","Track",255,255,nothing)
cv2.createTrackbar("US","Track",255,255,nothing)
cv2.createTrackbar("UV","Track",255,255,nothing)

while True:
    frame = cv2.imread('./images/smarties.png')

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH","Track")
    l_s = cv2.getTrackbarPos("LS","Track")
    l_v = cv2.getTrackbarPos("LV","Track")

    u_h = cv2.getTrackbarPos("UH","Track")
    u_s = cv2.getTrackbarPos("US","Track")
    u_v = cv2.getTrackbarPos("UV","Track")

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv,l_b,u_b)

    res = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("frame",frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
