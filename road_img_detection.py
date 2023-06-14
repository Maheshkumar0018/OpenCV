import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('./images/road1.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
print('image_shape: ',img.shape)
height = img.shape[0]
width = img.shape[1]
# ROI
region_of_Interest_vertices = [
    (0,height),
    (width/2,height/2),
    (width,height)
]

def region_of_interest(img,vertices):
    # black matrics that matches img h,w
    mask = np.zeros_like(img)
    # retrive no of color chanels from img
    #channel_count = img.shape[2] #img have 3 channel 
    # create a match color with same color channel_counts
    #match_mask_color = (255,)*channel_count #img have 3 channel
    match_mask_color = 255
    print("match_mask_color: ",match_mask_color)
    cv2.fillPoly(mask,vertices,match_mask_color)
    masked_img = cv2.bitwise_and(img,mask)
    return masked_img

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny_img = cv2.Canny(gray_img,100,200)

cropped_img = region_of_interest(canny_img,
                                 np.array([region_of_Interest_vertices],np.int32)) #img - if 3channels

# HoughlinesP
lines = cv2.HoughLinesP(cropped_img,
                        rho = 6,
                        theta=np.pi/60,
                        threshold=160,
                        lines=np.array([]),
                        minLineLength=40,
                        maxLineGap=25)

def draw_the_lines(img,lines):
    img = img.copy()
    # create blank img that matches original img
    blank_img = np.zeros((img.shape[0],img.shape[1],3),dtype=np.uint8)
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(blank_img,(x1,y1),(x2,y2),(255,255,0),thickness=4)
    img = cv2.addWeighted(img,0.8,blank_img,1,0.0)
    return img

img_with_lines = draw_the_lines(img,lines)

plt.imshow(cropped_img)
plt.imshow(img_with_lines)
plt.show()
cv2.destroyAllWindows()