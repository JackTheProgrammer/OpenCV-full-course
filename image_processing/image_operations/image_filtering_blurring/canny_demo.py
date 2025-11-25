import cv2
from pathlib import Path

try:
    from constants import IMAGES_FOLDER_PATH, SAVE_IMAGES_PATH
except ImportError:
    import sys
    sys.path.append(str(Path(__file__).resolve().parents[3]))
    from constants import IMAGES_FOLDER_PATH, SAVE_IMAGES_PATH

tulips_image_path = f"{IMAGES_FOLDER_PATH}tulip_hd.png"
image = cv2.imread(tulips_image_path)

# for RGB based images, use thresholds between 100-200
canny_rgb_edges = cv2.Canny(image, 100, 200)
cv2.imwrite(f"{SAVE_IMAGES_PATH}/tulips_rgb_canny_edges.png", canny_rgb_edges)
cv2.imshow("Original Image", image) 
cv2.imshow("Canny Edges - RGB Image", canny_rgb_edges)

# for grayscale based images, use thresholds between 50-150
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny_gray_edges = cv2.Canny(gray_image, 50, 150)
cv2.imwrite(f"{SAVE_IMAGES_PATH}/tulips_gray_canny_edges.png", canny_gray_edges)
cv2.imshow("Canny Edges - Grayscale Image", canny_gray_edges)

cv2.waitKey(0)
cv2.destroyAllWindows()

# import cv2
# import os
# import sys

# # 1. Check if the module was loaded
# if 'cv2' in sys.modules:
#     print("cv2 module is loaded.")
    
#     # 2. Print the path where Python FOUND the cv2 module
#     try:
#         cv2_path = cv2.__file__
#         print(f"\n✅ Python is loading 'cv2' from this location:")
#         print(f"   {cv2_path}")
        
#         # 3. Print the directory containing the loaded file
#         cv2_dir = os.path.dirname(cv2_path)
#         print(f"   Directory: {cv2_dir}")

#         # 4. Check for the missing attribute (will likely raise the error again)
#         print("\nChecking for cv2.imread...")
#         if hasattr(cv2, 'imread'):
#             print("Attribute 'imread' found. OpenCV is correctly loaded.")
#         else:
#             print("❌ Attribute 'imread' NOT found. The loaded module is NOT the real OpenCV.")
            
#     except AttributeError:
#         # This occurs if the loaded cv2 is a folder/package without a __file__ attribute,
#         # but often it works fine.
#         print("Error checking __file__. The conflict is likely local.")
# else:
#     print("cv2 module was not found in sys.modules.")