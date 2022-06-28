import cv2 as cv

# we resize and rescale images and video frames in opencv to prevent computational strain
# large media files tend to store a lot of information and displaying it takes a lot of processing

# rescaling a video implies modifying its height and width to a particular height and width
# generally 
img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75): # created a function to rescale frame, set a default value for scale
    # This method works for images, video, live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

# Resizing images
resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

def changeRes(width, height):
    # works only for live video. Does not work on standalone video files.
    capture.set(3, width)
    capture.set(4, height)

# Reading videos
capture = cv.VideoCapture('Videos/dog.mp4') # Capture variable is an instance of VideoCapture class
 
while True:
    isTrue, frame = capture.read() # Inside the while loop here, we can grab the video frame by frame by utilizing the capture.read() method 
    
    # frame_resized = rescaleFrame(frame)
    frame_resized = rescaleFrame(frame, scale = 0.2)

    cv.imshow('Video', frame) # each frame of the video is displayed by cv.imshow() method (passing window name and frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'): # This tells the system to stop displaying video if letter 'd' is pressed
        break

capture.release() # We then release capture device
cv.destroyAllWindows() # and we destroy all the windows