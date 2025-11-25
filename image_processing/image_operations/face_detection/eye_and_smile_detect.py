import sys
from pathlib import Path
from os.path import exists
import cv2

sys.path.append(str(Path(__file__).resolve().parents[3]))
from constants import FRONTAL_FACE_CASCADE_PATH, EYE_CASCADE_PATH, SMILE_CASCADE_PATH

if exists(FRONTAL_FACE_CASCADE_PATH) == False and exists(EYE_CASCADE_PATH) == False and exists(SMILE_CASCADE_PATH) == False:
    print(f"The paths are not valid.")

else:
    print("All required paths are valid.\nWe're good to go 👍👍")

    cam_video = cv2.VideoCapture(0)

    face_cascade = cv2.CascadeClassifier(FRONTAL_FACE_CASCADE_PATH)
    eye_cascade = cv2.CascadeClassifier(EYE_CASCADE_PATH)
    smile_cascade = cv2.CascadeClassifier(SMILE_CASCADE_PATH)

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
                roi_gray = gray_frame[y:y + h, x:x + w]
                roi_color = frame[y:y + h, x:x + w]

                # Detect eyes within the face region
                # The minNieghors is higher to reduce false positives by making
                # the detection stricter and scaleFactor is kept low to 
                # detect smaller eyes
                detected_eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=15)
                for (ex, ey, ew, eh) in detected_eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)
                    # Add text label for the eye (relative to ROI)
                    cv2.putText(roi_color, "Eye", (ex, ey - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)

                # Detect smiles within the face region
                # The minNeighbors is set high to avoid false positives and
                # scaleFactor is increased to detect larger smiles
                detected_smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.7, minNeighbors=22)
                for (sx, sy, sw, sh) in detected_smiles:
                    if sy > h / 2:  # To avoid detecting smiles in the eye region
                        cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)
                        # Add text label for the smile (relative to ROI)
                        cv2.putText(roi_color, "Smile", (sx, sy + sh + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

            cv2.imshow("Eye and Smile Detection", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

cam_video.release()
cv2.destroyAllWindows()