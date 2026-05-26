# Color detection system using OpenCV, Python
import cv2
import numpy as np
from  PIL import Image


def get_limits(color):

    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    hue = hsvC[0][0][0]

    if hue >= 165:
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([180, 255, 255], dtype=np.uint8)

    elif hue <= 15:
        lowerLimit = np.array([0, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)

    else:
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit

blue = [255,0,0]
cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    hsv= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #calling get_limits function
    lowerLimit, upperLimit = get_limits(color=blue)
    mask = cv2.inRange(hsv,lowerLimit, upperLimit)
    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),5)
    print(bbox)
    cv2.imshow('Gray scale image',frame)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cap.release()
cv2.destroyAllWindows()