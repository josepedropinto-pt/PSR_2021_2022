#!/usr/bin/env python3
import argparse
import cv2


def main():

    image_filename = 'image.jpg'
    # 1-color 0-black -1-original
    image = cv2.imread(image_filename, 0)  # Load an image
    cv2.imshow('image_test', image)  # Display the image
    cv2.waitKey(0)  # wait for a key press before proceeding


if __name__ == '__main__':
    main()
