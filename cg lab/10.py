import cv2
import numpy as np


img = cv2.imread('12.jpg')

gau = cv2.GaussianBlur(img,(5,5),0)
med = cv2.medianBlur(img,5)
bil = cv2.bilateralFilter(img,9,75,75)

cv2.imshow("scl_img",gau)
cv2.imshow("trans_img",med)
cv2.imshow("ans_img",bil)

cv2.waitKey(0)
cv2.destroyAllWindows()