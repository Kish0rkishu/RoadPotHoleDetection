import cv2
import numpy as np


img = cv2.imread('12.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edge = cv2.Canny(gray,200,100)

kernel = np.ones((5,5),np.float32)/25

texture = cv2.filter2D(gray,-1,kernel)

cv2.imshow("rot_img",gray)
cv2.imshow("scl_img",edge)
cv2.imshow("trans_img",kernel)
cv2.imshow("ans_img",texture)

cv2.waitKey(0)
cv2.destroyAllWindows()