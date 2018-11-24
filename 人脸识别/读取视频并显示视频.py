# encoding=utf-8
import cv2
 
# 处理视频类
# 参数是文件名就是读取视频文件
camera = cv2.VideoCapture("bike.avi")
# python语法，用缩进表示代码块，相当于c的括号
while True:
    # 读取一帧图像,ret为是否读到的返回值，img为读到的图像
    (ok, img) = camera.read()
    if not ok:
        print "open video failed"
        break
    else:
        print "open video success"
        cv2.imshow("videoCapture", img)
    if cv2.waitKey(33) & 0xFF == ord('q'):  # 等待33毫秒,输入q跳出
        break
 
camera.release()    #释放摄像头
cv2.destroyAllWindows() #销毁所有设备
 
cv2.waitKey(0);  # 等待输入
