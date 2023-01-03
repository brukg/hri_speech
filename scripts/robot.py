#!/usr/bin/env python3
import rospy

from geometry_msgs.msg import PoseStamped


class Robot():
    def __init__(self):
        self.name = "Robot"
        self.pub_goal = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
    def say(self, text):
        print(text)
    
    def goto(self, place):
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

    
