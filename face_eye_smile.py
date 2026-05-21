import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

capture = cv2.VideoCapture(0)

while True:

    ret, frame = capture.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    detect_face = face_cascade.detectMultiScale(gray, 1.2, 5)

    for (x, y, w, h) in detect_face:

        # face rectangle
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

        # ROI
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # Top half only for eyes
        eye_roi_gray = roi_gray[0:h // 2, 0:w]
        eye_roi_color = roi_color[0:h // 2, 0:w]

        eyes = eye_cascade.detectMultiScale(eye_roi_gray, 1.1, 10)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(eye_roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 4)
        if len(eyes) > 0:
            cv2.putText(
                frame,
                'Eyes Detected',
                (x, y-30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0,255,0),
                2
            )

        # Bottom half only for smile
        smile_roi_gray = roi_gray[h // 2:, 0:w]
        smile_roi_color = roi_color[h // 2:, 0:w]

        smile = smile_cascade.detectMultiScale(smile_roi_gray, 1.7, 20)  # higher minNeighbors = less false positives
        for (sx, sy, sw, sh) in smile:
            cv2.rectangle(smile_roi_color, (sx, sy), (sx + sw, sy + sh), (0, 255, 255), 4)
        if len(smile) > 0:
            cv2.putText(
                frame,
                'Smile Detected',
                (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0,0,255),
                2
            )

    cv2.imshow('Face_Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

capture.release()
cv2.destroyAllWindows()