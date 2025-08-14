import glob
import cv2
import numpy as np
for im in glob.glob("D:/16/HW_WCS_17/*"):
    img = cv2.imread(im.replace('/', '\\'))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, binary_mask = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY_INV)  # Detect dark areas (black lines)

    # Step 4: Refine the mask (optional)
    kernel = np.ones((3, 3), np.uint8)
    refined_mask = cv2.dilate(binary_mask, kernel, iterations=1)  # Dilate to ensure line coverage

    # Step 5: Inpaint the image
    repaired = cv2.inpaint(img, refined_mask, inpaintRadius=1, flags=cv2.INPAINT_TELEA)
    denoised = cv2.medianBlur(repaired, 3)
    final = cv2.fastNlMeansDenoisingColored(denoised, None, 10, 10, 9, 30)
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])

    # Apply the sharpening kernel
    sharpened = cv2.filter2D(final, -1, kernel)

    cv2.waitKey()
    cv2.destroyAllWindows()
    cv2.imwrite("D:\\16\\17_denoised\\"+im[15:],sharpened)