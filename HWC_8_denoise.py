import glob
import cv2
import numpy as np
for im in glob.glob("D:/16/HW_WCS_8/*"):
     image = cv2.imread(im.replace('/', '\\'), cv2.IMREAD_GRAYSCALE)
     _, binary = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY_INV)
     column_sums = np.sum(binary, axis=0)
     gap_columns = np.where(column_sums < 10)
     mask = np.zeros_like(image)
     mask[:, gap_columns] = 255
     img = cv2.inpaint(image, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)
     cv2.imwrite("D:\\16\\8_denoised\\" + im[14:], img)
