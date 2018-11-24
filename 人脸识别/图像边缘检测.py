#encoding=utf-8
import cv2
import numpy as np #数学工具包
 
img = cv2.imread("./images/Lena.jpg")
#边缘检测1
gray =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   #转换为灰度图，以便运算
lab = cv2.Laplacian(img, cv2.CV_64F)    #深度
lab = np.uint8(np.absolute(lab))    #绝对值化
cv2.imshow("laplacain", lab)
 
#边缘检测2
#canny像素值范围30到150
canny = cv2.Canny(img, 30, 150)
cv2.imshow("canny", canny)
 
cv2.waitKey(0)
