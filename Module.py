import cv2

path = 'D:/Python/xu li anh/stm32.png'

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


