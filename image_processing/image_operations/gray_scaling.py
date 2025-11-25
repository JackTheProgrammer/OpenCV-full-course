import cv2

image = cv2.imread('image_processing/use_image/mattar ke pakode.jfif')
if image is None:
    print("Error: Could not read the image.")
else:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray Mattar ke Pakode', gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()