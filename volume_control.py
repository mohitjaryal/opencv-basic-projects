from math import sqrt
import mediapipe as mp
import cv2
import os
import time

# webcam start
webCam = cv2.VideoCapture(0)

# MediaPipe hands model
myHands = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

x1 = y1 = 0
x2 = y2 = 0

prev_time = 0

while True:
    _, image = webCam.read()

    # frame size
    frame_height, frame_width, _ = image.shape

    # convert BGR to RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # detect hands
    output = myHands.process(rgb_image)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:

            drawing_utils.draw_landmarks(image, hand)
            landmarks = hand.landmark

            for id, lm in enumerate(landmarks):

                x = int(lm.x * frame_width)
                y = int(lm.y * frame_height)

                # index finger tip
                if id == 8:
                    x1, y1 = x, y
                    cv2.circle(image, (x, y), 10, (0, 255, 255), 3)

                # thumb tip
                if id == 4:
                    x2, y2 = x, y
                    cv2.circle(image, (x, y), 10, (0, 0, 255), 3)

            # distance calculation
            dist = sqrt((x2 - x1)**2 + (y2 - y1)**2) / 4

            # cooldown
            current_time = time.time()

            if current_time - prev_time > 0.5:

                # volume control using MacOS command
                if dist > 50:
                    os.system("osascript -e 'set volume output volume (output volume of (get volume settings) + 10)'")
                else:
                    os.system("osascript -e 'set volume output volume (output volume of (get volume settings) - 10)'")

                prev_time = current_time

            # line between fingers
            cv2.line(image, (x1, y1), (x2, y2), (0, 255, 255), 3)

    cv2.imshow("video", image)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

webCam.release()
cv2.destroyAllWindows()