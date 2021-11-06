#!/usr/bin/env python

import cv2 as cv
import numpy as np


def main():

    # import original image and convert to HSV
    original_image = cv.imread('atlas2000_e_atlasmv.png', 1)
    original_hsv = cv.cvtColor(original_image, cv.COLOR_BGR2HSV)
    cv.imshow('original_RGB', original_image)
    cv.imshow('original_HSV', original_hsv)

    # mask the green box and print the mask
    lower_thresh = np.array([60, 230, 80])
    upper_thresh = np.array([70, 250, 105])
    mask_green_box = cv.inRange(original_hsv, lower_thresh, upper_thresh)
    cv.imshow('mask_green_box', mask_green_box)

    # print the mask on the original image
    green_box = cv.bitwise_and\
        (original_image, original_image, mask=mask_green_box)
    cv.imshow('green box', green_box)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()







