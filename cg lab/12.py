import cv2
import cv2.data
import numpy as np

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

img = cv2.imread('12.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(img,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("ans_img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()