#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from aula9_excs.msg import SpecialDog


def callback(msg):
    rospy.loginfo("Received a dog named " + msg.name + "which is " + str(msg.age) + " years old")


def main():

    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber("chatter", SpecialDog, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    main()