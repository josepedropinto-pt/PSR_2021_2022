#!/usr/bin/env python3


import cv2 as cv
import matplotlib.pyplot as plt


def main():
    image = cv.imread('atlascar2.png', 0)
    _, th1 = cv.threshold(image, 128, 255, cv.THRESH_BINARY)
    _, th2 = cv.threshold(image, 128, 255, cv.THRESH_OTSU)

    cv.imshow('Threshold_1', th1)
    cv.imshow('Original', image)
    cv.imshow('Threshold_2', th2)

    cv.waitKey(0)


if __name__ == '__main__':
    main()
