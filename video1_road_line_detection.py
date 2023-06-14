import cv2
import numpy as np

# ROI - cropped img
def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_img = cv2.bitwise_and(img, mask)
    return masked_img

# draw lines on img
def draw_the_lines(img, lines):
    img = img.copy()
    blank_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_img, (x1, y1), (x2, y2), (0, 255, 0), thickness=3)
    img = cv2.addWeighted(img, 0.8, blank_img, 1, 0.0)
    return img

def process(image):
    height = image.shape[0]
    width = image.shape[1]
    
    region_of_interest_vertices = [
        (0, height),
        (width/2, height/2),
        (width, height)
    ]
    gray_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    canny_edge = cv2.Canny(gray_img, 200, 255)

    cropped_img = region_of_interest(canny_edge,
                                     np.array([region_of_interest_vertices], np.int32))
    lines = cv2.HoughLinesP(cropped_img,
                            rho=6,
                            theta=np.pi/60,
                            threshold=160,
                            lines=np.array([]),
                            minLineLength=40,
                            maxLineGap=25)
    img_with_lines = draw_the_lines(image, lines)
    return img_with_lines

# capturing video
cap = cv2.VideoCapture('./videos/solidWhiteRight.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        if frame is not None:
            frame = process(frame)
            cv2.imshow('Frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    else:
        break

cap.release()
cv2.destroyAllWindows()
