import cv2
import numpy as np 
import matplotlib.pyplot as plt

img = cv2.imread('img/sudoku-photo-2.jpg')
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray_copy = gray.copy()

blur = cv2.GaussianBlur(gray_copy,(9,9),0)

thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11,2)