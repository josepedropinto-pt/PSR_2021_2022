#!/usr/bin/env python3

import cv2 as cv


def main():
    image = cv.imread('atlascar2.png', 0)

    # type prints the type of the variable
    print(type(image))  # 'numpy.ndarray'

    # shape prints the size of image
    print(image.shape)
    # output (450, 600, 1); (lines, columns, channels)

    # print the datatype of numpy elements
    print(image.dtype)
    # output uint8

    # using numpy library to threshold image
    image_threshold = image > 128
    # cv.imshow('numpy threshold', image_threshold)
    print(image_threshold.dtype)
    # output bool

    # using cv library to compare differences between images
    _, th1 = cv.threshold(image, 128, 255, cv.THRESH_BINARY)
    cv.imshow('threshold_binary', th1)

    cv.waitKey(0)


if __name__ == '__main__':
    main()
