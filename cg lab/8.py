import cv2
import numpy as np

img = cv2.imread('12.jpg')
height,width,_ = img.shape
rota_mat = cv2.getRotationMatrix2D((width/2,height/2),90,1)
scal_mat = np.float32([[1.5,0,0],[0,1.5,0]])
trans_mat = np.float32([[1,0,100],[0,1,50]])

rota_img = cv2.warpAffine(img,rota_mat,(width,height))
scal_img = cv2.warpAffine(img,scal_mat,(int(width*1.5),int(height*1.5)))
trans_img = cv2.warpAffine(img,trans_mat,(width,height))

cv2.imshow("originalimg",img)
cv2.imshow("rotatedimg",rota_img)
cv2.imshow("scalingimg",scal_img)
cv2.imshow("translatedimg",trans_img)
cv2.waitKey(0)
cv2.destroyAllWindows()