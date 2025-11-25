import cv2
from pathlib import Path
import numpy as np

try:
    from constants import LOW_RES_IMAGE_PATH, SAVE_IMAGES_PATH
except ImportError:
    import sys
    sys.path.append(str(Path(__file__).resolve().parents[3]))
    from constants import LOW_RES_IMAGE_PATH, SAVE_IMAGES_PATH

image = cv2.imread(LOW_RES_IMAGE_PATH)
ddepth = -1
kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])
gaussian_filtered_image = cv2.filter2D(image, ddepth, kernel)
cv2.imwrite(f"{SAVE_IMAGES_PATH}/gaussian_filtered_image.jpg", gaussian_filtered_image)
cv2.imshow("Original Image", image)
cv2.imshow("Gaussian Filtered Image", gaussian_filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()