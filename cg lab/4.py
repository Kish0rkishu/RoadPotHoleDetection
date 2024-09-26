import cv2
import numpy as np

canvas_width = 800
canvas_height = 600

canvas = np.ones((canvas_width,canvas_height,3),dtype=np.uint8)*255
obj_points = np.array([[100,100],[200,100],[200,200],[100,200]],dtype=np.int32)

tran_matr = np.float32([[1,0,100],[0,1,50]])
rot_matr = cv2.getRotationMatrix2D([150,150],45,1)
scal_matr = np.float32([[1.5,0,0],[0,1.5,0]])

tran_img = np.array([np.dot(tran_matr,[x,y,1])[:2]for x,y in obj_points],dtype= np.int32)
rot_img = np.array([np.dot(rot_matr,[x,y,1])[:2]for x,y in tran_img],dtype= np.int32)
scal_img = np.array([np.dot(scal_matr,[x,y,1])[:2]for x,y in rot_img],dtype= np.int32)

cv2.polylines(canvas,[obj_points],True,(0,0,0),2)
cv2.polylines(canvas,[tran_img],True,(0,255,0),2)
cv2.polylines(canvas,[rot_img],True,(255,0,0),2)
cv2.polylines(canvas,[scal_img],True,(0,0,255),2)

cv2.imshow("2D Translation",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()