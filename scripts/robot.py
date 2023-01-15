#!/usr/bin/env python3
import rospy

from geometry_msgs.msg import PoseStamped
import pyttsx3


class Robot():
    def __init__(self):
        self.name = "Robot"
        self.pub_goal = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
        self.engine = pyttsx3.init()

    def say(self, text):
        print(text)
        self.engine.say(text)
        self.engine.runAndWait()


    def call(self, action, place):
        if action == "go":
            self.goto(place)
        elif action == "stop":
            self.say("Stopping")
            self.stop()
        elif action == "answer":
            if len(place) > 0:
                self.say(place)
    def stop(self):
        pass

    def goto(self, place):
        self.say("Going to the" + place)
        if place == "kitchen":
            self.move(1, 2)
        elif place == "bedroom":
            self.move(2, 0)
        elif place == "living room":
            self.move(-2, 1)
        elif place == "bathroom":
            self.move(-7, 4)
        else:
            self.say("I don't know where is " + place)
    def move(self, x, y):
        print("Moving to x: " + str(x) + ", y: " + str(y))
        goal = PoseStamped()
        goal.header.frame_id = "map"
        goal.pose.position.x = x
        goal.pose.position.y = y
        goal.pose.orientation.w = 1.0
        self.pub_goal.publish(goal)

    
