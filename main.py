import cv2

webcam = cv2.VideoCapture(0)
while True:
    _, img = webcam.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    cv2.imshow('Frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
webcam.release()
cv2.destroyAllWindows()


# # In ra độ rộng và cao của ảnh
# img = cv2.imread('stm32.PNG')
# print('do cao anh: ', img.shape[0])
# print('do rong anh: ', img.shape[1])
# cv2.imshow('Anh goc', img)

# # Resize lại kích thước ảnh
# img2 = cv2.resize(img,(1080,720))
# cv2.imshow('Anh resize', img2)

# cv2.imwrite("test.png", img2)
# # Ấn phím bất kì mới tắt
# cv2.waitKey()