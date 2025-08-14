import glob
import cv2
for im in glob.glob("D:/16/HW_WCS_7/*"):
     img = cv2.imread(im.replace('/', '\\'))
     _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
     img=cv2.erode(img,(3,3),iterations=3)
     cv2.imwrite("D:\\16\\7_denoised\\" + im[14:], img)