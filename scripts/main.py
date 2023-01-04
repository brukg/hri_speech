#!/usr/bin/env python3

import rospy
import numpy as np
import rospkg
from deep_speech import DeepSpeech
from whisper_speech import WhisperSpeech
from gesture_controller import GestureController
from robot import Robot
#create a class for ros node
class RosNode:
    def __init__(self):
        #create a publisher
        # self.pub = rospy.Publisher('chatter', String, queue_size=10)
        # #create a subscriber
        # self.sub = rospy.Subscriber('chatter', String, self.callback)
        # #create a service
        # self.srv = rospy.Service('chatter', String, self.service_callback)
        # #create a client
        # self.client = rospy.ServiceProxy('chatter', String)

        self.robot = Robot()

        self.ds_model = rospkg.RosPack().get_path('hri_speech') + '/models/deepspeech-0.9.3-models.pbmm'
        self.ds_scorer = rospkg.RosPack().get_path('hri_speech') + '/models/deepspeech-0.9.3-models.scorer'
        # self.deep_speech = DeepSpeech(self.ds_model, self.ds_scorer, self.robot)

        self.whisper = WhisperSpeech(self.robot)
        self.gesture_control = GestureController()
        # #create a timer
        self.timer = rospy.Timer(rospy.Duration(1), self.timer_callback)

    # def callback(self, msg):
    #     #do something with the message
    #     pass

    # def service_callback(self, req):
    #     #do something with the request
    #     return StringResponse("response")

    def timer_callback(self, event):
        #do something
        pass
    
    def listen_microphone(self):
        data = self.stream.read(1024)
        data16 = np.frombuffer(data, dtype=np.int16)
        print(self.model.stt(data16))

if __name__ == '__main__':
    rospy.init_node('ros_node')
    node = RosNode()
    rospy.spin()