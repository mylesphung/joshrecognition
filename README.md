# joshrecognition
Joshrecognition is a combination of two face recognition scripts: picture.py, and webcam.py. Picture.py inputs a picture, and finds faces in the picture. Webcam.py uses your webcam, and tracks faces in the webcam through a live feed. The facial recognition identifiers are from the Haar Cascade- I didn't make them myself.

**Note:**
webcam.py may need some configuring, if your device has multiple webcams. The device I tested it on, a Surface laptop, had three accessible cameras: the front, rear, and infrared (for Windows Hello). If the webcam program is using the wrong camera, go into the script and change the VideoCapture value in parenthesis (there should be a note next to it). The values start at 0, and will change depending on your device.

Modules needed:
- cv2
- sys

Caveats:
- Facial recognition identifiers come from the Haar Cascade, and while they generally work well, they aren't perfect- the most common issue would be counting the number of faces incorrectly (which is both an openCV and Haar Cascade issue)
- Webcam.py has a hard time recognizing faces when the faces are moving quickly

No commit history for the files because I finished all of the programs before uploading to GitHub. 
<br/>Name "joshrecognition" comes from my friend Josh, whose face was the first to be tested with this program.
