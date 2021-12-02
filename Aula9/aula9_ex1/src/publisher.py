#!/usr/bin/env python
import argparse

import colorama
import rospy
from colorama import Fore
from std_msgs.msg import String
from aula9_ex1.msg import SpecialDog


def talker():
    # First initialize node
    rospy.init_node('talker', anonymous=True)

    # Create publisher
    pub = rospy.Publisher('chatter', SpecialDog, queue_size=10)
    frequency = rospy.get_param("~frequency", default=1)

    # Define Rate
    rate = rospy.Rate(frequency)  # 10hz

    while not rospy.is_shutdown():

        text_color = rospy.get_param("/highlight_text_color")

        dog = SpecialDog()
        dog.name = 'max'
        dog.age = 18
        dog.color = 'pink'
        dog.brothers.append('boby')
        dog.brothers.append('lassie')

        rospy.loginfo('publishing the dogs name: ' + getattr(colorama.Fore, text_color) + str(dog.name) + Fore.RESET)
        pub.publish(dog)
        rate.sleep()


if __name__ == '__main__':
    talker()
