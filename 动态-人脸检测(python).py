import cv2  
import numpy as np  
  
cv2.namedWindow("test")  
cap = cv2.VideoCapture(0) #加载摄像头录制  
# cap = cv2.VideoCapture("test.mp4") #打开视频文件  
success, frame = cap.read()  
# classifier = cv2.CascadeClassifier("/Users/yuki/anaconda/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml")  # 确保此xml文件与该py文件在一个文件夹下，否则将这里改为绝对路径  
 
#haarcascade_frontalface_default.xml
classifier = cv2.CascadeClassifier("/Users/yuki/anaconda/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml")  # 确保此xml文件与该py文件在一个文件夹下，否则将这里改为绝对路径  
 
while success:  
    success, frame = cap.read()  
    size = frame.shape[:2]  
    image = np.zeros(size, dtype=np.float16)  
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
    cv2.equalizeHist(image, image)  
    divisor = 8  
    h, w = size  
    minSize = (w // divisor, h // divisor)  
    faceRects = classifier.detectMultiScale(image, 1.2, 2, cv2.CASCADE_SCALE_IMAGE, minSize)  
    if len(faceRects) > 0:  
        for faceRect in faceRects:  
            x, y, w, h = faceRect  
            cv2.rectangle(frame,(x,y),(x+h,y+w),(0,255,0),2)
            #锁定 眼和嘴巴
#             cv2.circle(frame, (x + w // 4, y + h // 4 + 30), min(w // 8, h // 8), (255, 0, 0))   # 左眼
#             cv2.circle(frame, (x + 3 * w //4, y + h // 4 + 30), min(w // 8, h // 8), (255, 0, 0))   #右眼
#             cv2.rectangle(frame, (x + 3 * w // 8, y + 3 * h // 4), (x + 5 * w // 8, y + 7 * h // 8), (255, 0, 0))   #嘴巴
    cv2.imshow("test", frame)  
    key = cv2.waitKey(10)  
    c = chr(key & 255)  
    if c in ['q', 'Q', chr(27)]:  
        break  
cv2.destroyWindow("test")  
