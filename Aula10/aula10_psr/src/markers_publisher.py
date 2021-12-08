#!/usr/bin/env python

from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
import rospy


def talker():

    # ---------------------------------------------------
    # Initialization
    # ---------------------------------------------------
    rospy.init_node('register', anonymous=False)
    publisher = rospy.Publisher('markers', Marker, queue_size=10)
    rospy.Rate(10)

    # ---------------------------------------------------
    # Execution
    # ---------------------------------------------------
    while not rospy.is_shutdown():

        # Marker Sphere
        marker_sphere = Marker()
        marker_sphere.header.frame_id = "map"
        marker_sphere.type = marker_sphere.SPHERE
        marker_sphere.action = marker_sphere.ADD
        marker_sphere.ns = 'sphere'
        marker_sphere.scale.x = 1
        marker_sphere.scale.y = 1
        marker_sphere.scale.z = 1
        marker_sphere.color.a = 0.5
        marker_sphere.color.r = 0
        marker_sphere.color.g = 1.0
        marker_sphere.color.b = 0
        marker_sphere.pose.orientation.w = 1.0
        marker_sphere.pose.orientation.x = 0
        marker_sphere.pose.orientation.y = 0
        marker_sphere.pose.orientation.z = 0
        marker_sphere.pose.position.x = 0
        marker_sphere.pose.position.y = 0
        marker_sphere.pose.position.z = 0

        # Marker Cube
        marker_cube = Marker()
        marker_cube.header.frame_id = "map"
        marker_cube.type = marker_cube.CUBE
        marker_cube.action = marker_cube.ADD
        marker_cube.ns = 'cube'
        marker_cube.scale.x = 0.5
        marker_cube.scale.y = 0.5
        marker_cube.scale.z = 0.5
        marker_cube.color.a = 1.0
        marker_cube.color.r = 1.0
        marker_cube.color.g = 0.0
        marker_cube.color.b = 0.0
        marker_cube.pose.orientation.w = 1.0
        marker_cube.pose.orientation.x = 0
        marker_cube.pose.orientation.y = 0
        marker_cube.pose.orientation.z = 0
        marker_cube.pose.position.x = 0
        marker_cube.pose.position.y = 0
        marker_cube.pose.position.z = 0

        # Marker Text
        marker_text = Marker()
        marker_text.header.frame_id = "map"
        marker_text.type = marker_text.TEXT_VIEW_FACING
        marker_text.action = marker_text.ADD
        marker_text.ns = 'Text'
        marker_text.text = 'Radius: 1'
        marker_text.scale.x = 0.5
        marker_text.scale.y = 0.5
        marker_text.scale.z = 0.5
        marker_text.color.a = 1.0
        marker_text.color.r = 1.0
        marker_text.color.g = 1.0
        marker_text.color.b = 0.0
        marker_text.pose.orientation.w = 1.0
        marker_text.pose.orientation.x = 30
        marker_text.pose.orientation.y = 0
        marker_text.pose.orientation.z = 0
        marker_text.pose.position.x = 1
        marker_text.pose.position.y = 1
        marker_text.pose.position.z = 1

        # markerArray.markers.append(marker_sphere)
        # # Renumber the marker_sphere IDs
        # id = 0
        # for m in markerArray.markers:
        #     m.id = id
        #     id += 1

        # Publish Markers
        rospy.loginfo('I am publishing')
        publisher.publish(marker_sphere)
        publisher.publish(marker_cube)
        publisher.publish(marker_text)
        rospy.sleep(0.01)


if __name__ == '__main__':
    talker()
