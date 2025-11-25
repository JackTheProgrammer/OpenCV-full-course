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
    text = 'Pakode'
    org = (60, 90)
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.1
    color = (0, 181, 253)  # Blue color in BGR
    thickness = 2
    textual_image = cv2.putText(image, text, org, font, font_scale, color, thickness)
    cv2.imshow("Image with Circle", textual_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()