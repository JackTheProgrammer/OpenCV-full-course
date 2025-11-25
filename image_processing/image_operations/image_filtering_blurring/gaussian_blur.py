import cv2
from pathlib import Path

try:
    from constants import CLEARED_IMAGE_PATH, SAVE_IMAGES_PATH
except ImportError:
    import sys
    sys.path.append(str(Path(__file__).resolve().parents[3]))
    from constants import CLEARED_IMAGE_PATH, SAVE_IMAGES_PATH

image = cv2.imread(CLEARED_IMAGE_PATH)
gaussian_blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
cv2.imwrite(f"{SAVE_IMAGES_PATH}/gaussian_blurred_image.jpg", gaussian_blurred_image)
cv2.imshow("Original Image", image)
cv2.imshow("Gaussian Blurred Image", gaussian_blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()