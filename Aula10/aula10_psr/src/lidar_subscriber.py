#!/usr/bin/env python

import rospy
from sensor_msgs import point_cloud2
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import PointCloud2, PointField
from std_msgs.msg import Header
import math

global pub


def callback(msg):
    global pub

    # Check print just for debug purpose
    no_messures = len(msg.ranges)
    rospy.loginfo("I received " + str(no_messures) + "measurements")

    # Run over all the distances to convert polar to cartesian coordinates
    points = []
    i = 0
    for dist in msg.ranges:
        theta = msg.angle_min + i * msg.angle_increment
        x = dist * math.cos(theta)
        y = dist * math.sin(theta)
        z = 0
        pt = [x, y, z]

        # Save coordinates into a list
        points.append(pt)
        i += 1

    # PointFields outputs the organized parameters to create point cloud
    fields = [PointField('x', 0, PointField.FLOAT32, 1),
              PointField('y', 4, PointField.FLOAT32, 1),
              PointField('z', 8, PointField.FLOAT32, 1)
              ]

    # Sets the header
    header = Header()
    header.frame_id = "left_laser"

    # Creates and publishes point cloud with chosen header, converted points, and defined fields
    pc2 = point_cloud2.create_cloud(header, fields, points)
    pub.publish(pc2)


def main():
    global pub

    rospy.init_node('subscriber', anonymous=False)
    rospy.Subscriber("/left_laser/laserscan", LaserScan, callback)

    # Creates the publisher with "Point_Cloud_test" topic and PointCloud2 type message
    pub = rospy.Publisher("Point_Cloud_test", PointCloud2, queue_size=10)

    rospy.spin()


if __name__ == '__main__':
    main()
