#encoding=utf-8
import cv2  #导入opencv2库
img = cv2.imread("./images/beach.jpg")   #载入图片，图片路径有两种斜杠
cv2.imshow("HelloCV", img)  #显示图像
cv2.imwrite("D:/save1.jpg", img)#保存图片
cv2.waitKey(0)  #等待用户输入键，退出
