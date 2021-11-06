#!/usr/bin/env python

import argparse
from functools import partial
import cv2 as cv


def onTrackbar(threshold, window_name, image_gray):
    # Function used on slider of the trackbar
    _, image_binary = cv.threshold(image_gray, threshold, 255,
                                   cv.THRESH_BINARY)
    # Preview of the slider effect
    cv.imshow(window_name, image_binary)


def onMouse(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print("The coordinates are " +
              str(x) + "," + str(y))

    # if event == cv.EVENT_RBUTTONDOWN:
    #     blue = image_gray[y, x, 0]
    #     green = image_gray[y, x, 1]
    #     red = image_gray[y, x, 2]
    #
    #     print('RGB : (' + str(red) + ' ' + str(green)
    #           + ' ' + str(blue))


def main():
    # Defining the argument parser to call the full path to image file
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str,
                        required=True, help='Full path to image file.')
    args = vars(parser.parse_args())

    # Reading the image and convert it to grayscale
    image = cv.imread(args['image'], 1)
    image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    window_name = 'window - Ex3b'
    cv.imshow(window_name, image_gray)

    # Partial func to call the OnTrackbar function fixing some parameters
    onTrackbar_call = partial(onTrackbar, window_name=window_name,
                              image_gray=image_gray)

    # Create trackbar ('name', 'window_name', 'default', 'max', func)
    cv.createTrackbar('binary', window_name, 0, 255, onTrackbar_call)

    # Creat mouse click event on "Window" with function "onMouse"
    cv.setMouseCallback(window_name, onMouse)

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
