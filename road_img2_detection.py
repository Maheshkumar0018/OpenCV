import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('./images/road2.jpg')
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

gary_img = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
canny_edge = cv2.Canny(gary_img,150,255)

height = image.shape[0]
width = image.shape[1]

region_of_interest_vertices = [
    (0,height),
    (width/2,height/2),
    (width,height)
]

# ROI - cropped img
def region_of_interest(img,vertices):
    # blank matrics have same size of image
    mask = np.zeros_like(img)
    match_mask_color = 255
    cv2.fillPoly(mask,vertices,match_mask_color)
    masked_img = cv2.bitwise_and(img,mask)
    return masked_img

cropped_img = region_of_interest(canny_edge,np.array([region_of_interest_vertices],np.int32))

# apply HoughlinesP
lines = cv2.HoughLinesP(cropped_img,
                        rho = 6,
                        theta=np.pi/60,
                        threshold=160,
                        lines=np.array([]),
                        minLineLength=40,
                        maxLineGap=25)

# draw lines on img
def draw_the_lines(img,lines):
    img = img.copy()
    # create blank img
    blank_img = np.zeros((img.shape[0],img.shape[1],3),dtype=np.uint8)
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(blank_img,(x1,y1),(x2,y2),(0,255,0),thickness=3)
    img = cv2.addWeighted(img,0.8,blank_img,1,0.0)
    return img

img_with_lines = draw_the_lines(image,lines)

plt.imshow(cropped_img)
plt.imshow(img_with_lines)
plt.show()
cv2.destroyAllWindows()