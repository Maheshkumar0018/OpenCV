import cv2
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Read the images
New_Zealand_Boat = cv2.imread('./images/New_Zealand_Boat.jpg')
New_Zealand_Lake = cv2.imread('./images/New_Zealand_Lake.jpg')
print("New_Zealand_Boat shape:", New_Zealand_Boat.shape)
print("New_Zealand_Lake shape:", New_Zealand_Lake.shape)

# Step 2: Generate Gaussian pyramid for both images
New_Zealand_Boat_copy = New_Zealand_Boat.copy()
gp_New_Zealand_Boat = [New_Zealand_Boat_copy]
for i in range(6):
    New_Zealand_Boat_copy = cv2.pyrDown(New_Zealand_Boat_copy)
    gp_New_Zealand_Boat.append(New_Zealand_Boat_copy)

New_Zealand_Lake_copy = New_Zealand_Lake.copy()
gp_New_Zealand_Lake = [New_Zealand_Lake_copy]
for i in range(6):
    New_Zealand_Lake_copy = cv2.pyrDown(New_Zealand_Lake_copy)
    gp_New_Zealand_Lake.append(New_Zealand_Lake_copy)

# Step 3: Generate Laplacian pyramid for both images
lp_New_Zealand_Boat = [gp_New_Zealand_Boat[5]]
for i in range(5, 0, -1):
    gaussian_expanded = cv2.pyrUp(gp_New_Zealand_Boat[i])
    laplacian = cv2.subtract(gp_New_Zealand_Boat[i-1], gaussian_expanded)
    lp_New_Zealand_Boat.append(laplacian)

lp_New_Zealand_Lake = [gp_New_Zealand_Lake[5]]
for i in range(5, 0, -1):
    gaussian_expanded = cv2.pyrUp(gp_New_Zealand_Lake[i])
    laplacian = cv2.subtract(gp_New_Zealand_Lake[i-1], gaussian_expanded)
    lp_New_Zealand_Lake.append(laplacian)

# Step 4: Blend the Laplacian pyramids
New_Zealand_Boat_New_Zealand_Lake_pyramid = []
for New_Zealand_Boat_lp, New_Zealand_Lake_lp in zip(lp_New_Zealand_Boat, lp_New_Zealand_Lake):
    cols, rows, ch = New_Zealand_Boat_lp.shape
    New_Zealand_Lake_lp_resized = cv2.resize(New_Zealand_Lake_lp, (rows, cols))
    laplacian = np.hstack((New_Zealand_Boat_lp[:, :int(cols/2)], New_Zealand_Lake_lp_resized[:, int(cols/2):]))
    New_Zealand_Boat_New_Zealand_Lake_pyramid.append(laplacian)

# Step 5: Reconstruct the blended image
New_Zealand_Boat_New_Zealand_Lake_reconstruct = New_Zealand_Boat_New_Zealand_Lake_pyramid[0]
for i in range(1, 6):
    New_Zealand_Boat_New_Zealand_Lake_reconstruct = cv2.pyrUp(New_Zealand_Boat_New_Zealand_Lake_reconstruct)
    New_Zealand_Boat_New_Zealand_Lake_reconstruct = cv2.add(New_Zealand_Boat_New_Zealand_Lake_pyramid[i],
                                                           New_Zealand_Boat_New_Zealand_Lake_reconstruct)

# Step 6: Display the images
cv2.imshow('New_Zealand_Boat', New_Zealand_Boat)
cv2.imshow('New_Zealand_Lake', New_Zealand_Lake)
cv2.imshow('New_Zealand_Boat_New_Zealand_Lake_reconstruct',
           New_Zealand_Boat_New_Zealand_Lake_reconstruct)
cv2.waitKey(0)
cv2.destroyAllWindows()
