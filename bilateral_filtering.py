import cv2
import numpy as np
# Read the image.
image = cv2.imread('images/train/61086.jpg')

# Apply bilateral filter with d = 15,
# sigmaColor = sigmaSpace = 75.
bilateral = cv2.bilateralFilter(image, 15, 75, 75)

cv2.imshow('original_image', image)
# Save the output.
cv2.imshow('bilateral', bilateral)
