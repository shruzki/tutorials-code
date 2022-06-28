import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

# plt.imshow(img)
# plt.show() # Matplotlib thinks it is RGB so colours are inverted

# BGR to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb) # OpenCV thinks it is BGR so colour inversion takes place

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv-bgr', hsv_bgr)

# LAB to BGR
lab_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('lab-bgr', lab_bgr)

# GRAY to BGR
gray_bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
cv.imshow('gray-bgr', gray_bgr)
# doubt!

# plt.imshow(rgb)
# plt.show() # No color inversion now

cv.waitKey(0)