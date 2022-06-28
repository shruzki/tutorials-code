import cv2 as cv
import sys

# Reading Images
#img = cv.imread('Photos/cat_large.jpg') 

#print(sys.getsizeof(img)) 
#print(sys.getsizeof(int))

#cv.imshow('Cat', img)
#cv.waitKey(0)

# Reading videos
# capture = cv.VideoCapture('Videos/dog.mp4') # Capture variable is an instance of VideoCapture class
# 
# while True:
#     isTrue, frame = capture.read() # Inside the while loop here, we can grab the video frame by frame by utilizing the capture.read() method 
#     cv.imshow('Video', frame) # each frame of the video is displayed by cv.imshow() method (passing window name and frame)
# 
#     if cv.waitKey(20) & 0xFF==ord('d'): # This tells the system to stop displaying video if letter 'd' is pressed
#         break
# 
# capture.release() # We then release capture device
# cv.destroyAllWindows() # and we destroy all the windows


#######
# we get the following error when opencv runs out of frames in videos:
# (-215:Assertion failed) size.width>0 && size.height>0 in function 'imshow'
#######
# we get similar error when we fail to provide correct path to an image:
# Reading Images
img = cv.imread('Photos/cat_large2.jpg') 

cv.imshow('Cat', img)
cv.waitKey(0)
# the error we get:
# cv2.error: OpenCV(4.5.5) /io/opencv/modules/highgui/src/window.cpp:1000: error: (-215:Assertion failed) size.width>0 && size.height>0 in function 'imshow'
