#!/usr/bin/env python

import rospy
from sensor_msgs import point_cloud2
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import PointCloud2, PointField
from std_msgs.msg import Header
from sensor_msgs.msg import Image
import math
from cv_bridge import CvBridge
import cv2 as cv
global pub, cv_image_rgb, cv_image_depth, bridge


def message_Depth_ReceivedCallback(message):
    global cv_image_depth
    global bridge
    global pub

    cv_image_depth = bridge.imgmsg_to_cv2(message, desired_encoding='passthrough')


def message_RGB_ReceivedCallback(message):
    global cv_image_rgb
    global bridge
    global pub

    cv_image_rgb = bridge.imgmsg_to_cv2(message, "bgr8")


def callback(msg):
    global pub, cv_image_rgb, cv_image_depth, bridge

    b, g, r = cv.split(cv_image_rgb)

    points = []

    x = 1
    y = 1
    z = 0
    pt = [x, y, z, r, g, b]

    # Save coordinates into a list
    points.append(pt)

    # PointFields outputs the organized parameters to create point cloud
    fields = [PointField('x', 0, PointField.FLOAT32, 1),
              PointField('y', 4, PointField.FLOAT32, 1),
              PointField('z', 8, PointField.FLOAT32, 1),
              PointField('r', 12, PointField.FLOAT32, 1),
              PointField('g', 16, PointField.FLOAT32, 1),
              PointField('b', 20, PointField.FLOAT32, 1)]

    # Sets the header
    header = Header()
    header.frame_id = "map"

    # Creates and publishes point cloud with chosen header, converted points, and defined fields
    pc2 = point_cloud2.create_cloud(header, fields, points)
    pub.publish(pc2)


def main():
    global pub, cv_image_rgb, cv_image_depth, bridge
    bridge = CvBridge()

    # Init node and create subscribers of image ond depth
    rospy.init_node('subscriber', anonymous=False)
    rospy.Subscriber("camera/rgb/image_raw", Image, message_RGB_ReceivedCallback)
    rospy.Subscriber("camera/depth/image_raw", Image, message_Depth_ReceivedCallback)

    # Creates the publisher with "Point_Cloud_rgbd" topic and PointCloud2 type message
    pub = rospy.Publisher("Point_Cloud_rgbd", PointCloud2, queue_size=10)
    rospy.sleep(0.1)


if __name__ == '__main__':
    main()
