#encoding=utf-8
import cv2
img = cv2.imread("./images/baboon2.jpg")
 
(B, G, R) = cv2.split(img)
 
cv2.imshow("blue", B)
cv2.imshow("green", G)
cv2.imshow("red", R)
 
merge = cv2.merge([B, G, R])
cv2.imshow("merge", merge)
cv2.waitKey(0)
