# encoding=utf-8
import cv2
 
# 处理视频类
# 摄像头编号0(默认) 1 2 3
camera = cv2.VideoCapture("bike.avi")
#获取原视频的码率和大小
fps = camera.get(cv2.cv.CV_CAP_PROP_FPS)
size = (int(camera.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
        int(camera.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
#创建视频文件，用于保存
#文件名、选择编码方式、每秒钟播放fps、视频尺寸
#运行时会弹出让你选择压缩方式的窗口，如果录制完成之后视频的大小为0kb，#可能是编码方式不行，可以安装#Xvid试一下
videosave = cv2.VideoWriter("bike22.avi", -1, fps, size)
 
# python语法，用缩进表示代码块，相当于c的括号
while True:
    # 读取一帧图像,ret为是否读到的返回值，img为读到的图像
    (ok, img) = camera.read()
    if not ok:
        #print "open video failed"
        break
    else:
        #print "open video success"
        videosave.write(img)
        cv2.imshow("videoCapture", img)
    if cv2.waitKey(33) & 0xFF == ord('q'):  # 等待33毫秒,输入q跳出
        break
 
camera.release()    #释放摄像头
videosave.release() #释放保存句柄
cv2.destroyAllWindows() #销毁所有设备
 
cv2.waitKey(0);  # 等待输入
