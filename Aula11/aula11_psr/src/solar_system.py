#!/usr/bin/env python
import rospy
import tf2_ros
import geometry_msgs.msg
from math import sin, cos, pi

# ---------------------------------------------------
# Creating a static broadcast tf
# ---------------------------------------------------
if __name__ == '__main__':

    rospy.init_node('Solar_system')
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()
    rospy.sleep(0.5)
    t.header.stamp = rospy.Time.now()

    # Parameters for planet characterization
    t.header.frame_id = rospy.get_param("~parent_name")
    t.child_frame_id = rospy.get_param("~child_name")

    velocity = rospy.get_param("~velocity")
    radius = rospy.get_param("~radius")
    angle = 0

# ---------------------------------------------------
# Execution of the transformations and broadcasting
# ---------------------------------------------------
    while not rospy.is_shutdown():

        # Translation transformations with polar coordinates
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

        # Rotating depending on velocity ratio
        angle += 0.001*velocity
        if angle > 2 * pi:
            angle = 0

    rospy.spin()
