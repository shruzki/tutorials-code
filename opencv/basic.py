import cv2 as cv

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT) # to increase or decrease blur, increase or decrease kernel size (odd number, odd number) 
cv.imshow('Blur', blur)

# Edge Cascade
# (Finding the edges present in image)
# many edge cascades are available - we'll be using canny edge detector (pretty famous)
# canny = cv.Canny(img, 125, 175) # numbers are two thresholds
# cv.imshow('Canny Edges', canny)

# reduce the edges by passing in blurred image
canny = cv.Canny(blur, 125, 175) # numbers are two thresholds
cv.imshow('Canny Edges', canny)

# Dilating the image
# (image can be dilated using a specific structuring element (canny edges))
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
# eroded = cv.erode(dilated, (3,3), iterations=1)
eroded = cv.erode(dilated, (7,7), iterations=3) # an attempt to get back edge cascade
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500))
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)