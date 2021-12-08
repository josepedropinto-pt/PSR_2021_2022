#!/usr/bin/env python

import cv2 as cv
import rospy
# from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


def talker():
    # ---------------------------------------------------
    # Initialization
    # ---------------------------------------------------

    # Initialize node
    rospy.init_node('images', anonymous=False)

    # Create publisher
    pub = rospy.Publisher('webcam_image', Image, queue_size=1)

    # Define Rate of publisher
    rospy.Rate(10)  # 10hz

    # Defining webcam and Bridge converting
    capture = cv.VideoCapture(0)
    bridge = CvBridge()

    # ---------------------------------------------------
    # Execution
    # ---------------------------------------------------
    while not rospy.is_shutdown():

        # Set the window name
        window_original_frame = 'python_webcam'

        # Read the capture video and resize it
        _, frame = capture.read()

        # Converting the webcam frame into ROS message
        image_message = bridge.cv2_to_imgmsg(frame, "bgr8")

        # Plot the image into the window created
        cv.namedWindow(window_original_frame, cv.WINDOW_NORMAL)
        cv.imshow(window_original_frame, frame)

        rospy.loginfo('I am publishing another image')
        pub.publish(image_message)

    # ---------------------------------------------------
    # Termination
    # ---------------------------------------------------
        if cv.waitKey(1) == ord('q'):
            break
    capture.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    talker()
