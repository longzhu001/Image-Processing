#encoding=utf-8
import cv2
 
img = cv2.imread("./images/beach.jpg")
 
print img.shape #像素宽高、3L为rgb三通道
print img.size#文件大小
 
#获得某个像素点的值
(b, g, r) = img[0, 0]
print b, g,  r
 
#得到一块图像,改变其颜色
img[0:100, 0:100] = (0, 255, 0)
cv2.imshow("100x100", img)
cv2.waitKey(0)
