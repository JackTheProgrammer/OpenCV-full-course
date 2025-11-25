import cv2
from pathlib import Path

try:
    from constants import NOISY_IMAGE_PATH, SAVE_IMAGES_PATH
except ImportError:
    import sys
    sys.path.append(str(Path(__file__).resolve().parents[3]))
    from constants import NOISY_IMAGE_PATH, SAVE_IMAGES_PATH

image = cv2.imread(NOISY_IMAGE_PATH)
median_blurred_image = cv2.medianBlur(image, 15)
cv2.imwrite(f"{SAVE_IMAGES_PATH}/balloons_denoised_image.png", median_blurred_image)
cv2.imshow("Original Image", image) 
cv2.imshow("Median Blurred Image", median_blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()