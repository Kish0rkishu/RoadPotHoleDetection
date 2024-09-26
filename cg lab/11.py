import cv2
import numpy as np


img = cv2.imread('12.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,tresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

counters,header = cv2.findContours(tresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

counter_img = img.copy()

cv2.drawContours(counter_img,counters,-1,(0,255,0),2)
cv2.imshow("ans_img",counter_img)

cv2.waitKey(0)
cv2.destroyAllWindows()