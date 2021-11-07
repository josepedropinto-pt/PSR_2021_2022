#!/usr/bin/env python

import argparse
from functools import partial
import cv2 as cv
import numpy as np


def func(x):
    pass


def onTrackbar(h_min, s_min, v_min, window_name, image_hsv):
    upper_thresh = np.array([255, 255, 255])

    threshed_image = cv.inRange(image_hsv, lower_thresh, upper_thresh)
    cv.imshow(window_name, threshed_image)


def main():
    # Defining the argument parser to call the full path to image file
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str,
                        required=True, help='Full path to image file.')
    args = vars(parser.parse_args())

    # Reading the image and convert it to grayscale
    image = cv.imread(args['image'], 1)
    # image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    window_name = 'window - Ex3b'
    cv.imshow(window_name, image)
    cv.namedWindow('trackbar')

    # Convert RGB to HSV
    image_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    # Partial func to call the OnTrackbar function fixing some parameters
    onTrackbar_call = partial(onTrackbar, window_name=window_name, image_hsv=image_hsv)

    # Create trackbar ('name', 'window_name', 'default', 'max', func)
    cv.createTrackbar('H_min', 'trackbar', 0, 255, func)
    cv.createTrackbar('S_min', 'trackbar', 0, 255, func)
    cv.createTrackbar('V_min', 'trackbar', 0, 255, func)

    h_min = cv.getTrackbarPos('H_min', 'trackbar')
    s_min = cv.getTrackbarPos('S_min', 'trackbar')
    v_min = cv.getTrackbarPos('V_min', 'trackbar')
    h_ma = cv.getTrackbarPos('H_min', 'trackbar')
    s_min = cv.getTrackbarPos('S_min', 'trackbar')
    v_min = cv.getTrackbarPos('V_min', 'trackbar')

    lower_thresh = np.array([h_min, s_min, v_min])
    upper_thresh = np.array([])
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
