import cv2
import winsound

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')



while True:
    ret, img = cap.read()

    faces = face_cascade.detectMultiScale(img, scaleFactor=1.5, minNeighbors=5, minSize=(20, 20))



    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    beep = face_cascade.detectMultiScale(img, scaleFactor=1.5, minNeighbors=5, minSize=(20, 20))
    for (x, y, w, h) in beep:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        winsound.Beep(500, 150)


    cv2.imshow('camera', img)
    if cv2.waitKey(10) == 27: # Клавиша Esc
        break

cap.release()
cv2.destroyAllWindows()







# User can beep a 1010 Hz tone for 110 milliseconds:


  # Beep at 1010 Hz for 110 milliseconds
