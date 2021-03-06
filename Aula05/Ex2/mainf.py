#!/usr/bin/env python

import cv2 as cv
import numpy as np


def main():

    # Import original image and convert to HSV
    original_image = cv.imread('../../../PSR_Assignment2_P2_G11/atlas2000_e_atlasmv.png', 1)
    original_hsv = cv.cvtColor(original_image, cv.COLOR_BGR2HSV)
    # cv.imshow('original_RGB', original_image)
    # cv.imshow('original_HSV', original_hsv)

    # Mask the green box and print the mask
    lower_thresh = np.array([50, 128, 50])
    upper_thresh = np.array([100, 255, 100])
    mask_green_box = cv.inRange(original_hsv, lower_thresh, upper_thresh)
    cv.imshow('mask_green_box', mask_green_box)

    # Print the mask on the original image
    green_box = cv.bitwise_and \
        (original_image, original_image, mask=mask_green_box)
    cv.imshow('green box', green_box)

    # Copy new original image to print red box
    original_copy = original_image.copy()

    # Paint the masked box with another color
    red_box = cv.add(original_image, (0, 0, 255, 0),
                     mask=mask_green_box, dst=original_copy)
    # Function add uses merges 2 images or image and scalar with
    # a defined mask into a specific destination
    cv.imshow('original changed', original_copy)
    # cv.imshow('red box', red_box) same output why?

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
