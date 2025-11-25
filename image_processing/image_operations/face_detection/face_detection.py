import sys
from pathlib import Path
from os.path import exists
import cv2

sys.path.append(str(Path(__file__).resolve().parents[3]))
from constants import FRONTAL_FACE_CASCADE_PATH

if exists(FRONTAL_FACE_CASCADE_PATH) == False:
    print(f"The path {FRONTAL_FACE_CASCADE_PATH} is not a valid file.")

else:
    print("All required paths are valid.\nWe're good to go 👍👍")

    cam_video = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(FRONTAL_FACE_CASCADE_PATH)

    if not cam_video.isOpened():
        print("Error: Could not open video.")
        sys.exit()

    while True:
        ret, frame = cam_video.read()
        if ret == False:
            print("Failed to grab frame")
            break
        elif frame is None:
            print("No frame captured from camera")
            break
        else:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            detected_faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)
            for (x, y, w, h) in detected_faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.imshow("Face Detection", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

cam_video.release()
cv2.destroyAllWindows()