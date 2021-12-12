#!/usr/bin/env python3

import cv2
import argparse


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-path ', '--Path_to_Image', type=str,
                    help='Please type path to file')
    args = vars(ap.parse_args())
    image_filename = args['Path_to_Image']
    print(args)
    exit(0)
    image = cv2.imread(image_filename, 1)
    cv2.imshow('Test_atlas', image)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
