import cv2
from pathlib import Path

try:
    from constants import SAVE_IMAGES_PATH, IMAGES_FOLDER_PATH
except ImportError:
    import sys
    sys.path.append(str(Path(__file__).resolve().parents[3]))
    from constants import SAVE_IMAGES_PATH, IMAGES_FOLDER_PATH

img_path = f"{IMAGES_FOLDER_PATH}traingle_hq.png"
image = cv2.imread(img_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, threshold = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    cv2.drawContours(image, [cnt], 0, (0, 255, 0), 3)

cv2.imwrite(f"{SAVE_IMAGES_PATH}/contour_drawn_image.png", image)
cv2.imshow("Contour Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()