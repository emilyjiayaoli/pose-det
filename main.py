# from the mediaipe website for pose

import cv2
import mediapipe as mp
import body_tracking_module as btm

# referenced mediapipe documentation https://google.github.io/mediapipe/solutions/pose.html
#            pyautogui documentation for p.press("key") https://pyautogui.readthedocs.io/en/latest/keyboard.html
body = btm.PoseTracking() #takes in image

cap = cv2.VideoCapture(0)

slash = 0
block = 0
down = 0

while cap.isOpened():
    # reads image from webcam
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame!")
        continue

    # optionally mark the image as not writeable to pass by inference
    image.flags.writeable = False

    keypoints = body.get_kpts_list(image, True) #processes keypoints
    print(keypoints)

    # display image
    cv2.imshow('Pose Estimation!', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()