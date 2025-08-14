
import glob
import cv2
for im in glob.glob("D:/19/*"):
     img = cv2.imread(im.replace('/', '\\'),0)
     img = cv2.GaussianBlur(img, (3, 3), 1)
     _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
     img = cv2.resize(img, (200, 40), interpolation=cv2.INTER_AREA)
     cv2.waitKey()
     cv2.destroyAllWindows()
     cv2.imwrite("D:\\16\\19_denoised\\" + im[5:], img)
