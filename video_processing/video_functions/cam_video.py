import cv2

camera_cap = cv2.VideoCapture(0)

while True:
    ret, frame = camera_cap.read()
    if not ret:
        break

    cv2.imshow('Camera Feed', frame)

    # cv2.waitKey returns a 32-bit integer, so we
    # use bitwise AND with 0xFF to get the last 8 bits
    if cv2.waitKey(1) & 0xFF == ord('q'): # Press 'q' to exit
        print("Exiting camera feed.")
        break

camera_cap.release()
cv2.destroyAllWindows()