#encoding=utf-8
import cv2
import numpy as ny #别名
img = cv2.imread("./images/bear.jpg")
w = img.shape[0]
h = img.shape[1]
#平移图像
#创建一个变换矩阵
#平移：x轴正方向(1,0) 100， y轴正方向(0,1)50
M = ny.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(img, M, (w, h))#平移图像
cv2.imshow("Hello", dst)
cv2.imshow("HelloCV", img)
 
#旋转图像
#创建旋转矩阵，参数为旋转中心，旋转角度，缩放比例
N = cv2.getRotationMatrix2D((0.5*w, 0.5*h), 45, 0.75)
dst1 = cv2.warpAffine(img, N, (w, h))
cv2.imshow("HelloCV1", dst1)
cv2.waitKey(0)
