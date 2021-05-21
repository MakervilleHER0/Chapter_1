# Take a Photo with your webcam using Python

# Import the libraries you'll need for this script
import numpy as np
import sys
import cv2

# check the versions of your libraries
print (f"opencv2 version: {(cv2.__version__)} - Must be v3.4.x")
print (f"numpy version: {(np.__version__)}")
print (f"python version: {(sys.version)} - Must be v3.x")

# define a video capture object
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #Integrated camera
# cap = cv2.VideoCapture(1) USB camera

# Capture the image frame
ret, frame = cap.read()

# save the photo as a jpg image
cv2.imwrite('1Photo-NEW.jpg',frame)

# All done, release device
cap.release()
cv2.destroyAllWindows()
