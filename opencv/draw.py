import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype = 'uint8') # creating a blank image - give (height, width, no of channel colours)
cv.imshow('Blank', blank)

# 1. Paint the image a certain colour
# blank[:] = 0,255,0
# cv.imshow('Green', blank)

# blank[:] = 0,0,255
# cv.imshow('Red', blank)

# Drawing a portion of image
# blank[200:300, 300:400] = 0, 0, 255
# cv.imshow('Square', blank)

# 2. Draw a rectangle
# cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=2) # Outline only
# cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=cv.FILLED) # Filled
# cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=-1) # Alternate to get Filled
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1) # Alternate to get Filled
# cv.imshow('Rectangle', blank)

# 3. Draw a circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3) # (image, (coordinates), radius, color, thicnkess)
# cv.imshow('Circle', blank)

# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1) # (image, (coordinates), radius, color, thicnkess)
# cv.imshow('Circle', blank)

# 4. Draw a line
# cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=3)
# cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2) # img, text, org (coordinates), color, thickness=None
cv.imshow('Text', blank)

cv.waitKey(0)