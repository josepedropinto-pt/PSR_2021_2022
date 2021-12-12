#!/usr/bin/env python
import rospy
import tf2_ros

if __name__ == '__main__':

    # Creating the node and a buffer from the lister to accumulate info
    rospy.init_node('mercury_to_moon')
    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)
    rate = rospy.Rate(10.0)

    while not rospy.is_shutdown():
        try:
            # Get every transform from path
            # trans_1 = tfBuffer.lookup_transform('Sol', 'Mercury', rospy.Time(0))
            # trans_2 = tfBuffer.lookup_transform('Sol', 'Terra', rospy.Time(0))
            # trans_3 = tfBuffer.lookup_transform('Terra', 'Moon', rospy.Time(0))

            trans_simple = tfBuffer.lookup_transform('Mercury', 'Moon', rospy.Time(0))
            x = trans_simple.transform.translation.x
            y = trans_simple.transform.translation.y

            # Extract x,y values from transformations
            # x = trans_1.transform.translation[0]
            # y = trans_1.transform.translation[1]
            #
            # x1 = trans_2.transform.translation[0]
            # y1 = trans_2.transform.translation[1]
            #
            # x2 = trans_3.transform.translation[0]
            # y2 = trans_3.transform.translation[1]
            dist = round((x ** 2 + y ** 2) ** 0.5, 2)*100
            print('The distance from Mercury to Moon is aprox: ' + str(dist) + ' Milion Km')

        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue

        rate.sleep()
