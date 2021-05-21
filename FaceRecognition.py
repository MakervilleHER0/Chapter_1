# Use face recognition to determine the person in front of your webcam

# Import the libraries
import cv2
from cv2 import *
import numpy as np
from numpy import *
import face_recognition
import dlib
import PIL
from PIL import Image
import os
import time
import sys

# Print versions
print (f"opencv2 version: {(cv2.__version__)} - Must be v3.4.x")
print (f"numpy version: {(np.__version__)}")
print (f"python version: {(sys.version)} - Must be v3.x")
print (f"face_recognition version: {(face_recognition.__version__)}")
print (f"dlib version: {(dlib.__version__)}")
print (f"pillow version: {(PIL.__version__)}")

"""
REQUIRED VERSIONS:
~~~~~~~~~~~~~~~~~~~~
opencv2 version: 3.4.10          (MUST BE THIS VERSION)
numpy version: 1.19.5 or 1.20.2  (latest should be fine)
sys version: 3.6.6 or 3.9.5      (latest 3.x version should be fine)
face_recognition version: 1.2.3  (latest should be fine)
dlib version: 19.22.0            (latest should be fine)
pillow version: 8.2.0            (latest should be fine)
"""

# haarcascades for detecting - front view of the face
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.VideoCapture(0,cv2.CAP_DSHOW)

# Load the known images
face_image_0 = face_recognition.load_image_file("Mark.jpg")
face_image_1 = face_recognition.load_image_file("Chris.jpg")
face_image_2 = face_recognition.load_image_file("Andrew.jpg")
face_image_3 = face_recognition.load_image_file("David.jpg")
face_image_4 = face_recognition.load_image_file("John.jpg")
face_image_5 = face_recognition.load_image_file("Jen.jpg")
face_image_6 = face_recognition.load_image_file("Amanda.jpg")

# Get the face encoding of each person. This can fail if faces not found
face_encoding_0 = face_recognition.face_encodings(face_image_0)[0]
face_encoding_1 = face_recognition.face_encodings(face_image_1)[0]
face_encoding_2 = face_recognition.face_encodings(face_image_2)[0]
face_encoding_3 = face_recognition.face_encodings(face_image_3)[0]
face_encoding_4 = face_recognition.face_encodings(face_image_4)[0]
face_encoding_5 = face_recognition.face_encodings(face_image_5)[0]
face_encoding_6 = face_recognition.face_encodings(face_image_6)[0]

# Create a list of known face encodings
known_face_encodings = [
    face_encoding_0,
    face_encoding_1,
    face_encoding_2,
    face_encoding_3,
    face_encoding_4,
    face_encoding_5,
    face_encoding_6
]

# Check video for person
while(True):
    _,f=img.read()
    gray = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
            cv2.rectangle(f,(x,y),(x+w,y+h),(255,0,0),2)
            print("-")
            ret, frame = img.read()

            # Person found, save image for comparison
            cv2.imwrite('1Photo-NEW.jpg',frame)

            # Load the image we want to check
            unknown_image = face_recognition.load_image_file('1Photo-NEW.jpg')

            # Get face recognitions for any people in the picture
            unknown_face_encodings = face_recognition.face_encodings(unknown_image)

            # There might be more than 1 person, loop for each face
            for unknown_face_encoding in unknown_face_encodings:

                # Test if this unknow_face_encoding matches any known people
                results = face_recognition.compare_faces(known_face_encodings, unknown_face_encoding)
                name = "Unknown"
                if results[0]:
                    name = "Mark"
                elif results[1]:
                    name = "Chris"
                elif results[2]:
                    name = "Andrew"
                elif results[3]:
                    name = "David"
                elif results[4]:
                    name = "John"
                elif results[5]:
                    name = "Jen"
                elif results[6]:
                    name = "Amanda"

                print(f"Hi {name}!! I see you")

    # End program when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print("END")
img.release()
cv2.destroyAllWindows()

