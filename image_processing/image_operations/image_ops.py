import cv2

image = cv2.imread('use_image/mattar ke pakode.jfif')
if image is None:
    print("Error: Could not read the image.")
else:
    cv2.imshow('mattar ke pakode', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()