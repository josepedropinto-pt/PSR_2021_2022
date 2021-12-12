#!/usr/bin/env python

import argparse
import cv2 as cv

# Global variables
window_name = 'window - Ex3a'
image_gray = None


def onTrackbar(threshold):
    _, image_binary = cv.threshold(image_gray, threshold, 255,
                                   cv.THRESH_BINARY)
    cv.imshow(window_name, image_binary)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str,
                        required=True, help='Full path to image file.')
    args = vars(parser.parse_args())

    image = cv.imread(args['image'], 1)  # Load an image in color
    global image_gray  # use global var
    image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # convert bgr to gray image (single channel)
    cv.imshow(window_name, image_gray)

    cv.createTrackbar('binary', window_name, 0, 255, onTrackbar)

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
