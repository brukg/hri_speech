
#import google media pipe
import cv2
import mediapipe as mp
import numpy as np
import rospy


class GestureController:
    def __init__(self):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5)
        self.timer = rospy.Timer(rospy.Duration(1), self.timer_callback)
        print("GestureController initialized")

    def timer_callback(self, event):
        # data = self.stream.read(1024)
        # data16 = np.frombuffer(data, dtype=np.int16)
        # print(self.model.stt(data16))
        pass