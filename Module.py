import cv2
import os
import datetime

path = 'D:/Python/xu li anh/huy 1.jpg'
# mylist = os.listdir(path)

# images = []
# imgLabel = []

# for cl in mylist:
#     curimg=cv2.imread(f'{path}\\{cl}')
#     images.append(curimg)
#     imgLabel.append(os.path.splitext(cl)[0])

img = cv2.imread(path)
print('do cao anh:',img.shape[0])
print('do rong anh:',img.shape[1])
print('kich thuoc anh:',img.size)

# In ra độ cao - rộng - sâu của ảnh
# Ảnh màu có độ sâu = 3
# Ảnh đen trắng có độ sâu = 1
(h, w, d) = img.shape
print("Width = {}, Height = {}, Depth = {}".format(w, h, d))

(B, G, R) = img[50, 50]
print("R={}, G={}, B={}".format(R, G, B))

roi = img[50:350, 60:360]
cv2.imshow('Region Of Interest', roi)
cv2.waitKey(0)


