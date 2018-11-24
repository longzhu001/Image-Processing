#encoding=utf-8
import cv2
#动态图像追踪，两张图片相减
camera = cv2.VideoCapture("bike.avi")
#获取原视频的码率和大小
fps = camera.get(cv2.cv.CV_CAP_PROP_FPS)
size = (int(camera.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
        int(camera.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
#创建视频文件，用于保存
#文件名、选择编码方式、每秒钟播放fps、视频尺寸
videosave = cv2.VideoWriter("readbike.avi", -1, fps, size)
#初始化视频流的第一帧
firstFrame = None
 
while True:
    (ok, img) = camera.read()
    if not ok:
        print "open video failed"
        break
 
    #调整图像的大小，转换为灰度图，进行高斯模糊（平滑）
    h = img.shape[0]
    w = img.shape[1]
    img = cv2.resize(img, (w, h), interpolation=cv2.INTER_CUBIC)  #调整大小
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   #灰度化
    gray = cv2.GaussianBlur(gray, (21, 21), 0)  #进行高斯平滑处理，图像矩阵、滤波窗口大小、标准差，取该像素周围窗口大小内像素的平均值
 
    #如果是第一帧
    if firstFrame is None:
        firstFrame = gray   #初始背景图
    #计算当前帧与背景图的不同
    frameData = cv2.absdiff(firstFrame, gray)
    #进行二值化处理，如果像素小于阈值25，就变成0，大于阈值变成255,
    thresh = cv2.threshold(frameData, 25, 255, cv2.THRESH_BINARY)[1]
    #膨胀：扩展阈值图像 填充孔洞
    thresh = cv2.dilate(thresh, None, iterations=2)
    #在阈值图像上寻找轮廓
    (cnts, ret) = cv2.findContours(thresh.copy(),
                                   cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)
    #遍历轮廓
    for c in cnts:
        #计算轮廓大小，忽略掉小于500的
        if cv2.contourArea(c) < 100:
            continue
        #计算轮廓的边界框，在当前帧中绘制
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
 
    cv2.imshow("readMove", img)
    cv2.imshow("thresh", thresh)
    cv2.imshow("frameData", frameData)
    videosave.write(img)
    if cv2.waitKey(33) & 0xFF == ord('q'):
        break
 
camera.release()
cv2.destroyAllWindows()
 
cv2.waitKey(0); #等待输入
