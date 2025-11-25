import cv2

image = cv2.imread('use_image/mattar ke pakode.jfif')
if image is not None:
    print("Image shape", image.shape)
    resized_image = cv2.resize(image, (400, 400), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite('resized_image.png', resized_image)
    print("Resized image shape", resized_image.shape)
    cv2.imshow('Resized Image', resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Image not found or unable to load.")