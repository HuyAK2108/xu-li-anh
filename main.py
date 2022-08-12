import cv2
import numpy as np

# In ra độ rộng và cao của ảnh
img = cv2.imread('stm32.PNG')
print('do cao anh: ', img.shape[0])
print('do rong anh: ', img.shape[1])
cv2.imshow('Anh goc', img)

# Resize lại kích thước ảnh
img2 = cv2.resize(img,(1080,720))
cv2.imshow('Anh resize', img2)

cv2.imwrite("test.png", img2)
# Ấn phím bất kì mới tắt
cv2.waitKey()