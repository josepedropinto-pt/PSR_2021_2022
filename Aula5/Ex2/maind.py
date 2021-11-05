#!/usr/bin/env python

import cv2 as cv
import numpy as np


def main():

    # import the original image and show it
    original_image = cv.imread('atlas2000_e_atlasmv.png', 1)
    cv.imshow('original', original_image)
    cv.waitKey(0)

    # split the channels of the image
    (B, G, R) = cv.split(original_image)
    print(B.shape)
    # output(480, 720) only 1 channel

    # mask the green box with RGB segmentation
    lower_thresh = np.array([0, 65, 0])
    upper_thresh = np.array([50, 255, 50])


    # inRange uses the original_image and 2 threshold values
    mask_green_box = cv.inRange \
        (original_image, lower_thresh, upper_thresh)
    cv.imshow('mask_green_box', mask_green_box)

    # use mask to print on the original image
    green_box_image = cv.bitwise_and \
        (original_image, original_image, mask=mask_green_box)
    cv.imshow('green_box_image', green_box_image)
    cv.waitKey(0)

    # HSV conversion and mask conversion to HSV
    original_hsv = cv.cvtColor(original_image, cv.COLOR_BGR2HSV)
    lower = np.array([[[0, 65, 0]]])
    lower_hsv = cv.cvtColor(lower, cv.COLOR_BGR2HSV)
    print(lower_hsv)
    print()


if __name__ == "__main__":
    main()
