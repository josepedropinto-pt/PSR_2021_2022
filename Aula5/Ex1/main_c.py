#!/usr/bin/env python3

import cv2


def main():
    image1 = cv2.imread('atlascar.png', 1)
    image2 = cv2.imread('atlascar2.png', 1)

    flip = False

    while True:

        if flip:
            cv2.imshow('First_Atlas_Window', image1)
            flip = False
        else:
            cv2.imshow('Second_Atlas_Window', image2)
            flip = True

        q = cv2.waitKey(300)
        if q == 113:
            break


if __name__ == '__main__':
    main()
