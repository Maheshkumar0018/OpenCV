import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./images/Piano_Sheet_Music.png', cv2.IMREAD_GRAYSCALE)

def nothing(x):
    pass

# Create a window
cv2.namedWindow('Tracking')

# Create trackbars
cv2.createTrackbar('min', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('max', 'Tracking', 0, 255, nothing)

while True:
    # Get current trackbar positions
    min_val = cv2.getTrackbarPos('min', 'Tracking')
    max_val = cv2.getTrackbarPos('max', 'Tracking')

    # Apply Canny edge detection
    canny = cv2.Canny(img, min_val, max_val)

    # Display images
    #cv2.imshow('Original', img)
    cv2.imshow('Canny', canny)

    # Break the loop when 'Esc' key is pressed
    if cv2.waitKey(1) == 27:
        break

# Destroy all windows
cv2.destroyAllWindows()
