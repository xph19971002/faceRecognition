# -*- coding: utf-8 -*-
__author__ = 'xi'
__date__ = '2019/2/22 9:06'

import cv2
import time

print(cv2.__version__)
# G:\11.GitHub Repositories\faceRecognition\static\img\1.jpg
img = cv2.imread("")
print(img)
time.sleep(2)
cv2.namedWindow('Image')
cv2.imshow('Image', img)


cv2.waitKey(2)
cv2.destroyAllWindows()
