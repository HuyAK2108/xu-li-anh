import cv2
import numpy as np

img = cv2.imread('anh.PNG')
print('do cao anh: ', img.shape[0])
print('do rong anh: ', img.shape[1])

img2 = cv2.resize(img,(256,256))
cv2.imshow('Anh resize', img2)
cv2.waitKey()