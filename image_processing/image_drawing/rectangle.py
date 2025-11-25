import cv2
from pathlib import Path

try:
    # Prefer normal import when running as module from project root
    from constants import USE_IMAGE_PATH
except ModuleNotFoundError:
    # When the script is executed directly from inside the shapes/ folder
    # (for example, by clicking the file in the editor), Python's sys.path
    # may not include the project root. Add the parent directory of this
    # file (the project root) to sys.path and retry the import.
    import sys
    sys.path.append(str(Path(__file__).resolve().parents[2]))
    from constants import USE_IMAGE_PATH

image = cv2.imread(f'{USE_IMAGE_PATH}')
if image is None:
    raise FileNotFoundError(f"Image not found at path: {USE_IMAGE_PATH}")
else:
    print(f"Image loaded successfully from {USE_IMAGE_PATH}")
    height, width, _ = image.shape
    pt1 = (int(width * 0.1), int(height * 0.1))
    pt2 = (int(width * 0.9), int(height * 0.9))
    color = (0, 255, 0)  # Green color in BGR
    thickness = 3
    rect_image = cv2.rectangle(image, pt1, pt2, color, thickness)
    cv2.imshow("Image with Rectangle", rect_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()