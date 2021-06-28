

import cv2
import numpy as np
import matplotlib.pyplot as plt

background = cv2.createBackgroundSubtractorMOG2(history=5,varThreshold=5,detectShadows=True)

capture = cv2.VideoCapture(0)
if not capture.isOpened():
    exit(0)
while True:
    ret,frame = capture.read()
    if frame is None:
        break

    foreground_mask = background.apply(frame)

    cv2.imshow('Frame',frame)
    cv2.imshow("FG Mask",foreground_mask)

    k = cv2.waitKey(30)
    if k == ord("q"):
        break
capture.release()
cv2.destroyAllWindows()
cv2.waitKey(1)