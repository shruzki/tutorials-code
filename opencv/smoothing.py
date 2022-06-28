import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

# Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)
average7 = cv.blur(img, (7,7))
cv.imshow('7x7 Average Blur', average7)

# Gaussian Blur
# this is like weighted averaging (this kind of blur is more natural)
gauss = cv.GaussianBlur(img, (7,7), 0) # sigmaX is the standard deviation in x direction
cv.imshow('Gaussian Blur', gauss)

# Median Blur
# same as averaging except it finds median instead of average. more effective than mean in terms of reducing noise
median = cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)
# median blur is usually not effective for high kernel sizes

# Bilateral
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)