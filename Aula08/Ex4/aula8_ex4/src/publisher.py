#!/usr/bin/env python
# license removed for brevity
import argparse

import rospy
from std_msgs.msg import String
from aula8_ex4.msg import Dog


def talker():
    parser = argparse.ArgumentParser()

    parser.add_argument('-m',
                        '--message',
                        type=str,
                        required=True,
                        default="olá mundo",
                        help='Full path to json file.')

    args = vars(parser.parse_args())

    # First initialize node
    rospy.init_node('talker', anonymous=True)

    # Create publisher
    pub = rospy.Publisher('chatter', String, queue_size=10)

    # Define Rate
    rate = rospy.Rate(10)  # 10hz

    dog = Dog(name='Bobbi', age=7, color='Black')
    dog.addBrother('Lassie')
    while not rospy.is_shutdown():
        text_to_send = args['message'] + str(rospy.get_time())
        rospy.loginfo(text_to_send)
        pub.publish(text_to_send)
        rate.sleep()


if __name__ == '__main__':
    talker()
