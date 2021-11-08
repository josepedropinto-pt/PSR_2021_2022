#!/usr/bin/env python

import cv2 as cv
import numpy as np
import readchar

capture = cv.VideoCapture(0)

while True:
    # Set the window name
    window_name = 'Ex2 Frame'
    # Read the capture video and resize it
    _, image = capture.read()
    image = cv.resize(image, (800, 450))

    # Plot the image into the window created
    cv.imshow(window_name, image)

    # Close the window and break with "q" press
    if cv.waitKey(1) == ord('q'):
        break

capture.release()
cv.destroyAllWindows()


