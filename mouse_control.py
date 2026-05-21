# mouse control using Hand Gesture

import cv2
import mediapipe as mp
import pyautogui
import time
import math
cap = cv2.VideoCapture(0)
last_click = 0
myHands = mp.solutions.hands.Hands()
drawing_option = mp.solutions.drawing_utils
x1 = y1 = x2 = y2 = 0
screen_width, screen_height = pyautogui.size()
while True:
    _,image = cap.read()
    image = cv2.flip(image, 1)
    image_height, image_width, _ = image.shape
    rgb_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

    output_hands = myHands.process(rgb_image)
    hands = output_hands.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_option.draw_landmarks(image,hand) # draw points
            landmarks = hand.landmark # one hand landmark
            for id, lm in enumerate(landmarks):
                x = int(lm.x * image_width)
                y = int(lm.y * image_height)
                if id == 8:
                    mouse_x = int(screen_width / image_width * x)
                    mouse_y = int(screen_height / image_height * y)
                    cv2.circle(image,(x,y),5,(0,255,0),2)
                    pyautogui.moveTo(mouse_x,mouse_y,duration=0.1)
                    x1 =x
                    y1 = y
                if id == 4:
                    x2 = x
                    y2 = y
                    cv2.circle(image,(x,y),5,(0,255,0),2)
        dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        if dist < 40:  # tweak this value as needed
            if time.time() - last_click > 1:
                pyautogui.click()
                last_click = time.time()
    cv2.imshow('Hand movement video capture',image)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break


cap.release()
cv2.destroyAllWindows()