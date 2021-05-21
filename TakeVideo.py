# Show a video with your webcam using Python

# Import the libraries you'll need for this script
import cv2
import sys

# check the versions of your libraries
print (f"opencv2 version: {(cv2.__version__)} - Must be v3.4.x")
print (f"python version: {(sys.version)} - Must be v3.x")

vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Create a 'while' loop to get video (multiple frames) instead of a photo (single frame)
while(True):      
    ret, frame = vid.read()
    cv2.imshow('frame', frame)
      
    # Stop the video script by pressing the 'q' key on the keyboard
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the vid object and destroy all the windows
vid.release()
cv2.destroyAllWindows()
