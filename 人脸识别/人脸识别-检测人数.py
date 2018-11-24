# coding:utf-8

import sys

 
 '''
	人脸检测，以圆圈圈出人脸
	其中会识别图片的上有几个人脸,从而判断出途中人数是多少
 
 '''




import cv2

# 待检测的图片路径

imagepath = r'./heat.jpg'

 

# 获取训练好的人脸的参数数据，这里直接从GitHub上使用默认值

face_cascade = cv2.CascadeClassifier(r'./haarcascade_frontalface_default.xml')

 

# 读取图片

image = cv2.imread(imagepath)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

 

# 探测图片中的人脸

faces = face_cascade.detectMultiScale(

    gray,

    scaleFactor = 1.15,

    minNeighbors = 5,

    minSize = (5,5),

    flags = cv2.cv.CV_HAAR_SCALE_IMAGE

)

 

print "发现{0}个人脸!".format(len(faces))

 

for(x,y,w,h) in faces:

    # cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2)

    cv2.circle(image,((x+x+w)/2,(y+y+h)/2),w/2,(0,255,0),2)

 

cv2.imshow("Find Faces!",image)

cv2.waitKey(0)