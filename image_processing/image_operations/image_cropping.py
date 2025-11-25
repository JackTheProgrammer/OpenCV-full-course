import cv2

image = cv2.imread('use_image/mattar ke pakode.jfif')
if image is not None:
    print("Image shape", image.shape)
    cropped_image = image[103 : 206, 123 : 245]
    cv2.imwrite('cropped_image.png', cropped_image)
    cv2.imshow('cropped_image.png', cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()