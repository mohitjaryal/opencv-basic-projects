import cv2
import mediapipe as mp

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

cap = cv2.VideoCapture(0)

_,frame1 = cap.read()
result1 = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
while True:
    _, frame2 = cap.read()
    result2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    detect_face = face_cascade.detectMultiScale(result2, 1.2, 5)
    diff = cv2.absdiff(result1,result2)
    _, thresh = cv2.threshold(diff,20,255,cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # face
    for (x, y, w, h) in detect_face:
        face_diff = diff[y:y + h, x:x + w]
        if face_diff.mean() > 10:
            cv2.putText(frame2, 'Face is moving', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        else:
            cv2.putText(frame2, 'Face is still', (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)
        # face rectangle
        cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # draw  rectangle
    for contour in contours:
        if cv2.contourArea(contour) < 500:
            continue
        x,y,w,h = cv2.boundingRect(contour)
        cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cv2.putText(frame2,'Motion Detected',(300,300),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),2)

    cv2.imshow('frame1',thresh)
    cv2.imshow('frame2',frame2)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
    result1 =result2

cap.release()
cv2.destroyAllWindows()