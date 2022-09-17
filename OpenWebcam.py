import cv2

webcam = cv2.VideoCapture(0)

while True:
    _, img = webcam.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    fps = webcam.get(cv2.CAP_PROP_FPS)
    text = "FPS: {:.2f}".format(fps) 
    cv2.putText(img, text, (5, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 1)
    cv2.imshow('Webcam', img)
    print(fps)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    if cv2.waitKey(1) == 27:
        break
    
webcam.release()
cv2.destroyAllWindows()