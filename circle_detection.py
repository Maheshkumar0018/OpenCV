import cv2
import matplotlib.pyplot as plt
import numpy as np

# (x-x_center)**2 + (y-y_center)**2 = r**2
#dp: The inverse ratio of the accumulator resolution to the image resolution. It controls the resolution of the accumulator image. A smaller value detects smaller circles, while a larger value ignores smaller circles.
#minDist: The minimum distance between the centers of detected circles. It ensures that only one circle is detected within the specified minimum distance.
#param1: The higher threshold for the internal Canny edge detection used during the circle detection process.
#param2: The accumulator threshold for circle detection. It defines the minimum number of votes required for a circle to be detected.

img = cv2.imread('./images/smarties.png')
output = img.copy()
gray = cv2.cvtColor(output,cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray,5)

circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,dp=1,minDist=20,
                           param1=50,param2=30,minRadius=0,maxRadius=0)
detect_circles = np.uint16(np.around(circles))

for (x,y,r) in detect_circles[0,:]:
    print(x,y,r)
    cv2.circle(output,(x,y),r,(0,255,0),thickness=3)
    cv2.circle(output,(x,y),2,(0,255,255),thickness=3)


cv2.imshow('output',output)
cv2.waitKey(0)
cv2.destroyAllWindows()