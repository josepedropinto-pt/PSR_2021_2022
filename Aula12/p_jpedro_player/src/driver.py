#!/usr/bin/env python
# license removed for brevity

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist


class Driver:

    def __init__(self):
        self.publisher_command = rospy.Publisher('p_jpedro/cmd_vel', Twist, queue_size=10)

        rospy.Timer(rospy)


def talker():
    # ---------------------------------------------------
    # Initialization
    # ---------------------------------------------------
    rospy.init_node('p_jpedro_driver', anonymous=False)

    driver = Driver()

    rate = rospy.Rate(10)  # 10hz

    rospy.spin()
    # ---------------------------------------------------
    # Execution
    # ---------------------------------------------------
    while not rospy.is_shutdown():
        twist_msg = Twist()
        twist_msg.linear.x = 0.1
        twist_msg.angular.z = -1

        publisher.publish(twist_msg)
        rate.sleep()


if __name__ == '__main__':
    talker()
