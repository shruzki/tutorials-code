import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Edges', canny)

# we can do it without blur and canny - by threshold
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) # if intensity of pixel is <125: it is set to 0 (black); else: it is set to 255 (white); i.e., we convert image to binary
cv.imshow('Thresh', thresh)

# contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) # mode: cv.RETR_TREE (all hierarchical contours), cv.RETR_EXTERNAL (only external contours), cv.RETR_LIST (all contours)thod) # moIWWW
# contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE) # mode: cv.RETR_TREE (all hierarchical contours), cv.RETR_EXTERNAL (only external contours), cv.RETR_LIST (all contours)thod) # moIWWW
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) # mode: cv.RETR_TREE (all hierarchical contours), cv.RETR_EXTERNAL (only external contours), cv.RETR_LIST (all contours)thod) # moIWWW
print(f'{len(contours)} contour(s) found')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)


cv.waitKey(0)