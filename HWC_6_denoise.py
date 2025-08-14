import glob
import cv2
for im in glob.glob("D:/16/HW_WCS_6/*"):
     img = cv2.imread(im.replace('/', '\\'))
     img = cv2.flip(img, -1)
     img = cv2.blur(img, (3, 3), 1)
     _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
     cv2.imwrite("D:\\16\\6_denoised\\" + im[14:], img)