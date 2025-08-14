



import cv2
import os
import numpy as np
source_folder = 'D:/16/14_14'     # Folder with CAPTCHA images (with circles) D:/16/14_14
destination_folder = 'D:/16/14_denoised'  # Folder to save restored images

os.makedirs(destination_folder, exist_ok=True)

for filename in os.listdir(source_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(source_folder, filename)
        image = cv2.imread(image_path)

        # Convert to grayscale to detect the light gray circles
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect light gray regions (circle color is around 235)
        mask = cv2.inRange(gray, 180, 245)  # Fine-tune if needed

        # Optionally clean up the mask
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))
        mask = cv2.dilate(mask, kernel, iterations=1)
        mask = cv2.erode(mask, kernel, iterations=1)

        # Inpaint the masked regions using Telea's algorithm
        inpainted = cv2.inpaint(image, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)

        # Resize back if needed (200x40)
        inpainted = cv2.resize(inpainted, (200, 40), interpolation=cv2.INTER_AREA)

        # Save the repaired image
        destination_path = os.path.join(destination_folder, filename)
        cv2.imwrite(destination_path, inpainted)




