import cv2
import os
import numpy as np

source_folder = 'D:/16/HW_WCS_16'  # Overlapped images
destination_folder = 'D:/16/16_denoised'  # Output folder
0.
os.makedirs(destination_folder, exist_ok=True)

def undo_vertical_overlap(image):
    image = cv2.resize(image, (200, 40), interpolation=cv2.INTER_AREA)

    # Convert to float for precise operations
    img_f = image.astype(np.float32)

    # Create vertically shifted image (simulate what was used in blending)
    shifted_img = np.roll(img_f, shift=6, axis=1)
    shifted_img[:, :6] = 255  # Assume white background for new top rows

    # Approximate original image:
    # blend = 0.5 * original + 0.5 * shifted
    # => original ≈ 2 * blend - shifted
    recovered = 2 * img_f - shifted_img
    recovered = np.clip(recovered, 0, 255).astype(np.uint8)

    return recovered

for filename in os.listdir(source_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(source_folder, filename)
        img = cv2.imread(image_path)
        result = undo_vertical_overlap(img)

        save_path = os.path.join(destination_folder, filename)
        cv2.imwrite(save_path, result)

print("Horizontal overlap removal complete.")

