#!/usr/bin/env python


import argparse

import rospy
from colorama import Fore
from std_msgs.msg import String
from sensor_msgs.msg import Image
import cv2 as cv
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import String, Header
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import PointCloud2, PointField
from sensor_msgs import point_cloud2
import numpy as np

global cv_image_depth
global cv_image_rgb


def callback(message):
    global cv_image_rgb
    global cv_image_depth


def main():
    global cv_image_depth
    global cv_image_rgb

    # This declares that your node subscribes to the chatter topic which is of type std_msgs.msgs.String.

    rospy.init_node('subscriber_RGBD', anonymous=False)

    sub_depth = rospy.Subscriber('/camera/depth/image_raw', Image)
    sub_image = rospy.Subscriber('/camera/rgb/image_raw', Image)
    bridge = CvBridge()

    msg = np.zeros([100, 100, 3], dtype=np.uint8)
    cv_image_rgb = bridge.imgmsg_to_cv2(msg, "bgr8")
    cv_image_depth = bridge.imgmsg_to_cv2(sub_depth, desired_encoding='passthrough')

    cv.imshow('rgb', msg)
    cv.imshow('depth', cv_image_depth)

    b, g, r = cv.split(cv_image_rgb)
    print(cv_image_rgb.shape)
    print(cv_image_depth.shape)
    d = cv.split(cv_image_depth)


if __name__ == '__main__':
    main()
