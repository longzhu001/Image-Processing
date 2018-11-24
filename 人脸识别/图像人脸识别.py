#encoding=utf-8
import cv2
import numpy as np #数学工具包
 
img = cv2.imread("renlian2.jpg")#载入一张包含人脸的图片
 
cas = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")   #载入级联分类器，即人脸数据库
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转换为灰度图，以便运算
#检测人脸：跟数据库进行比较
#结果：人脸的坐标x, y, 长度, 宽度
rects = cas.detectMultiScale(gray)
 
for x, y, width, height in rects:
    cv2.rectangle(img, (x, y), (x+width, y+height), (0, 0, 255), 3)
 
cv2.imshow("face", img)
 
cv2.waitKey(0)
