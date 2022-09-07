# Python program to explain os.listdir() method 
    
# importing os module 
import os
import cv2
import numpy as np
# Get the path of current working directory
# path = os.getcwd()
path = 'D:/Python/xu li anh'
# Get the list of all files and directories
# in current working directory
dir_list = os.listdir(path)

# print("Files and directories in '", path, "' :") 
# print the list

face_detection  = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_detection   = cv2.CascadeClassifier( "haarcascade_eye.xml")
img     = cv2.imread('huy 2.jpg')
gray    = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces   = face_detection.detectMultiScale(gray, 1.3, 5)

img2 = cv2.imread('huy 2.jpg')
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
eyes = eye_detection.detectMultiScale(gray, 1.03, 5)

for (ex,ey,ew,eh) in eyes:
   img2 = cv2.rectangle(img2,(ex,ey),(ex+ew, ey+eh),(0,255,0),2)
cv2.imwrite('Eye_AB.jpg',img2)
# cv2.imshow('huy 1.jpg')

for (x,y,w,h) in faces:
   img = cv2.rectangle(img,(x,y),(x+w, y+h),(255,0,0),3)
cv2.imwrite('Face_huy.jpg',img)
# cv2.imshow('huy 1.jpg')



