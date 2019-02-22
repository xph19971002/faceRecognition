# -*- coding: utf-8 -*-
__author__ = 'xi'
__date__ = '2019/2/22 9:06'

import cv2

# print(cv2.__version__)

# 读取图片
file_path = "G:/11.GitHubRepositories/faceRecognition/static/img/1.jpg"
img = cv2.imread(file_path)

# 图片灰化
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 框 坐标轴设置
# x = y = 10
# 框 大小设置
# w = 100
# 框 颜色设置
color = (0, 0, 255)
# 绘制

# G:\11.GitHubRepositories\faceRecognition\EXT_RES\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml
# OpenCV人脸识别分类器
classifier = cv2.CascadeClassifier(
    "G:/11.GitHubRepositories/faceRecognition/EXT_RES/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml"
)
# 调用识别人脸
"""
分类器classifier.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))参数说明：

gray：转换的灰图

scaleFactor：图像缩放比例，可理解为相机的X倍镜

minNeighbors：对特征检测点周边多少有效点同时检测，这样可避免因选取的特征检测点太小而导致遗漏

minSize：特征检测点的最小尺寸
"""
faceRects = classifier.detectMultiScale(
    img_gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))

if len(faceRects):  # 大于0则检测到人脸
    for faceRect in faceRects:  # 单独框出每一张人脸
        x, y, w, h = faceRect
        # 框出人脸
        cv2.rectangle(img, (x, y), (x + h, y + w), color, 2)
        # 左眼
        cv2.circle(img, (x + w // 3, y + h // 8 + 18), min(w // 6, h // 6),
                   color, 2)
        # 右眼
        cv2.circle(img, (x + 3 * w // 4, y + h // 8 + 18), min(w // 6, h // 6),
                   color, 2)
        # 嘴巴
        cv2.rectangle(img, (x + 3 * w // 8, y + 3 * h // 4),
                      (x + 5 * w // 8, y + 7 * h // 8), color, 2)

# cv2.namedWindow("Girl")

# 显示
cv2.imshow("Baby Girl", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
