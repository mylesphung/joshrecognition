# import packages
import cv2
import sys

# Get user supplied values
imagePath = input("Path to image: ")
cascadePath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascadePath)

# Read the image
image = cv2.imread(imagePath)
grayScale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    grayScale,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = 0
)

print(f"Found {len(faces)} faces")

# Draw a rectangle around the faces
for (a, b, x, y) in faces:
    cv2.rectangle(image, (a, b), (a+x, b+y), (0, 255, 0), 2)

cv2.imshow("Faces found:", image)
cv2.waitKey(0)
