import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

mask = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Image', masked)

rectmask = cv.rectangle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), (img.shape[1]//2 + 100, img.shape[0]//2 + 100), 255, -1)
cv.imshow('Rectangle Mask', rectmask)

rectmasked = cv.bitwise_and(img, img, mask=rectmask)
cv.imshow('Rectangle masked image', rectmasked)

cv.waitKey(0)