import cv2

# This code reads an image, rotates it by 45 degrees around its center,
# and displays both the original and rotated images in separate windows.
# Finally, it saves the rotated image to a file.
image = cv2.imread('use_image/mattar ke pakode.jfif')
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imwrite('rotated_image_2d.png', rotated)
cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image', rotated)

print("Rotating image by -45 degrees")
# Additionally, rotate the image by -45 degrees and display/save it
print("Making changes for -45 degrees rotation")
M = cv2.getRotationMatrix2D(center, -45, 1.0)

print("Applying warpAffine for -45 degrees rotation")
rotated = cv2.warpAffine(image, M, (w, h))

print("Saving rotated image for -45 degrees rotation")
cv2.imwrite('rotated_image_neg_2d.png', rotated)

print("Displaying original and -45 degrees rotated images")
cv2.imshow('Original Image Negative', image)
cv2.imshow('Rotated Image Negative', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()