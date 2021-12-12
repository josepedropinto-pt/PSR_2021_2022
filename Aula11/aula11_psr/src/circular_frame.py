#!/usr/bin/env python
import rospy
import tf2_ros
import tf2_msgs.msg
import geometry_msgs.msg
from math import sin, cos, pi

# ---------------------------------------------------
# Creating a static broadcast tf
# ---------------------------------------------------
if __name__ == '__main__':

    rospy.init_node('Circular_Test')
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "parent"
    t.child_frame_id = "child"

    # Polar
    radius = 2
    angle = 0

# ---------------------------------------------------
# Execution of the transformations and broadcasting
# ---------------------------------------------------
    while not rospy.is_shutdown():

        t.transform.translation.x = radius * cos(angle)
        t.transform.translation.y = radius * sin(angle)
        t.transform.translation.z = 0.0

        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0
        rospy.loginfo(str(t.transform.translation.x) + "," + str(t.transform.translation.y))

        # Each transformation needs a new stamp
        t.header.stamp = rospy.Time.now()

        # Send Transformation "t" with broadcast "br"
        br.sendTransform(t)

        # Rotating 0.001 rad/per_iteration and start over after reaching 2pi
        angle += 0.001
        if angle > 2 * pi:
            angle = 0

    rospy.spin()
