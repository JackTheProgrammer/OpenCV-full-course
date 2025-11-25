import cv2

image = cv2.imread('use_image/mattar ke pakode.jfif')
flip_horizontal = cv2.flip(image, 1)
flip_vertical = cv2.flip(image, 0)
flip_both = cv2.flip(image, -1)
cv2.imshow('Original Image', image)
cv2.imshow('Flipped Horizontally', flip_horizontal)
cv2.imshow('Flipped Vertically', flip_vertical)
cv2.imshow('Flipped Both Axes', flip_both)
cv2.waitKey(0)
cv2.destroyAllWindows()