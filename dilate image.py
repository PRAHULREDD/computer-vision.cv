import cv2
import numpy as np

# Load the image (usually better on binary or edge images)
image = cv2.imread('input.jpg', 0)  # Load in grayscale

# Threshold the image (optional, useful for binary)
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Define kernel
kernel = np.ones((5, 5), np.uint8)

# Apply dilation
dilated = cv2.dilate(binary, kernel, iterations=1)

# Save the result
cv2.imwrite('dilated_output.jpg', dilated)

# Display (optional)
cv2.imshow('Original', image)
cv2.imshow('Dilated', dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()
