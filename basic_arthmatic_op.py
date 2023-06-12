import cv2

img = cv2.imread('./images/messi.jpg')
img2 = cv2.imread('./images/opencv_ologo.png')

print("Img 1 Shape: ",img.shape)
print("Img Size: ",img.size) # Total no of pixels
print("Img Dtype: ",img.dtype)

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r)) # pass channels in the for of tupple

# adding ball to image
ball = img[280:340,330:390] # ball coordinates
img[273:333,100:160] = ball

# image 2 resizing
# Resize img2 to match the size of img1
height, width, _ = img.shape
resized_img2 = cv2.resize(img2, (width, height))
print("Img 2 Shape: ",resized_img2.shape)

# 1. add
#dst = cv2.add(img,resized_img2)

# 2. addWeighted
dst = cv2.addWeighted(img,.9,resized_img2,.1,0)

cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()