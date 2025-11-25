import cv2
import numpy as np
from pathlib import Path

try:
    from constants import SAVE_IMAGES_PATH
except ImportError:
    import sys
    sys.path.append(str(Path(__file__).resolve().parents[3]))
    from constants import SAVE_IMAGES_PATH

"""
# IMPORTANT:
* The height and width of both images must be the same to perform bitwise operations.
* The number of channels in both images must also be the same.
* Bitwise operations are typically performed on binary images (black and white),
  but they can also be applied to grayscale or color images.
* The result of bitwise operations is also an image of the same size and type
  as the input images.
"""

img1 = np.zeros((300, 300, 3), dtype="uint8")
img2 = np.zeros((300, 300, 3), dtype="uint8")

cv2.circle(img1, (150, 150), 100, 255, -1)
cv2.rectangle(img2, (100, 100), (250, 250), (255, 255, 255), -1)

bitwise_and = cv2.bitwise_and(img1, img2)
bitwise_or = cv2.bitwise_or(img1, img2)
bitwise_xor = cv2.bitwise_xor(img1, img2)
bitwise_not_img1 = cv2.bitwise_not(img1)
bitwise_not_img2 = cv2.bitwise_not(img2)

cv2.imwrite(f"{SAVE_IMAGES_PATH}/bitwise_and.png", bitwise_and)
cv2.imwrite(f"{SAVE_IMAGES_PATH}/bitwise_or.png", bitwise_or)
cv2.imwrite(f"{SAVE_IMAGES_PATH}/bitwise_xor.png", bitwise_xor)
cv2.imwrite(f"{SAVE_IMAGES_PATH}/bitwise_not_img1.png", bitwise_not_img1)
cv2.imwrite(f"{SAVE_IMAGES_PATH}/bitwise_not_img2.png", bitwise_not_img2)

cv2.imshow("Circle Image", img1)
cv2.imshow("Rectangle Image", img2)
cv2.imshow("Bitwise AND", bitwise_and)
cv2.imshow("Bitwise OR", bitwise_or)
cv2.imshow("Bitwise XOR", bitwise_xor)
cv2.imshow("Bitwise NOT - Image 1", bitwise_not_img1)
cv2.imshow("Bitwise NOT - Image 2", bitwise_not_img2)

cv2.waitKey(0)
cv2.destroyAllWindows()