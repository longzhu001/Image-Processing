#encoding=utf-8
import cv2
img = cv2.imread("./images/beach.jpg")
red = (0, 0, 255)   #b g r
font = cv2.FONT_HERSHEY_COMPLEX_SMALL   #字体大小
cv2.putText(img, "asd", (100, 100), font, 4, red)
cv2.rectangle(img, (0, 0), (200, 200), red, -1) #粗细是-1，表示实心的图形
cv2.imshow("HelloCV", img)
cv2.waitKey(0)
