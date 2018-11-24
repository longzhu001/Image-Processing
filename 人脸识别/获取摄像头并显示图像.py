#encoding=utf-8
import cv2
 
#处理视频类
#摄像头编号0(默认) 1 2 3
camera = cv2.VideoCapture(0)    #必须要有参数，不写参数会导致读不到摄像头
#python语法，用缩进表示代码块，相当于c的括号
while True:
    # 读取一帧图像,ret为是否读到的返回值，img为读到的图像
    (ok, img) = camera.read()
    if not ok:
        print "open video failed"
        break
    else:
        print "open video success"
        cv2.imshow("videoCapture", img)
    if cv2.waitKey(33) & 0xFF == ord('q'):#等待33毫秒,输入q跳出
        break
 
camera.release()
cv2.destroyAllWindows()
 
cv2.waitKey(0); #等待输入
