import cv2
from pathlib import Path

try:
    from constants import IMAGES_FOLDER_PATH, SAVE_IMAGES_PATH
except ImportError:
    import sys
    sys.path.append(str(Path(__file__).resolve().parents[3]))
    from constants import IMAGES_FOLDER_PATH, SAVE_IMAGES_PATH

tulips_image_path = f"{IMAGES_FOLDER_PATH}tulip_hd.png"
image = cv2.imread(tulips_image_path, cv2.IMREAD_GRAYSCALE)
ret, thresh_img = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)
cv2.imwrite(f"{SAVE_IMAGES_PATH}/tulips_canny_binary_thresh.png", thresh_img)
cv2.imshow("Original Image", image)
cv2.imshow("Canny Edges - Binary Threshold Image", thresh_img)
cv2.waitKey(0)
cv2.destroyAllWindows()