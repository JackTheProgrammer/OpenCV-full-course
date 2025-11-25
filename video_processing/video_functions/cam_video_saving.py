import cv2 

camera_cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('video_processing/output/saved_cam_video.avi', fourcc, 20.0, (640, 480))
while True:
    ret, frame = camera_cap.read()
    if not ret:
        break

    out.write(frame)  # Save the frame to the video file

    cv2.imshow('Camera Feed', frame)

    # cv2.waitKey returns a 32-bit integer, so we
    # use bitwise AND with 0xFF to get the last 8 bits
    if cv2.waitKey(1) & 0xFF == ord('q'): # Press 'q' to exit
        print("Exiting camera feed and saving video.")
        break

camera_cap.release()
out.release()  # Release the video writer