# Imports
import cv2
import sys

# Gets the user input
cascadePath = "haarcascade_frontalface_default.xml"

# Creates the Cascade
faceCascade = cv2.CascadeClassifier(cascadePath)

# Sets the input source to the webcam
videoCapture = cv2.VideoCapture(1) ## change the value in parenthesis to change the camera

# Capture the frame by frame
while True:
    ret, frame = videoCapture.read()
    grayScale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        grayScale,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30)
    )
    # Draw the rectangle
    for (a, b, x, y)  in faces:
        cv2.rectangle(frame, (a,b), (a+x, b+y), (0, 255, 0), 2)

    # Display the result
    cv2.imshow('Face Detection: (press Q to exit)', frame)

    # Watching for the q key to end
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Once q is pressed, end
videoCapture.release()
cv2.destroyAllWindows()
