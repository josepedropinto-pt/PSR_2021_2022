#!/usr/bin/env python


import cv2 as cv


def main():
    # import original colored image
    image_colored = cv.imread('atlascar2.png', 1)
    print(image_colored.shape)
    #   output (450, 600, 3) -- 3 channel image

    # split the channels of the image
    (B, G, R) = cv.split(image_colored)
    cv.imshow('red', R)
    cv.imshow('green', G)
    cv.imshow('blue', B)

    # binary to the images
    _, th_b = cv.threshold(B, 50, 255, cv.THRESH_BINARY)
    _, th_g = cv.threshold(G, 100, 255, cv.THRESH_BINARY)
    _, th_r = cv.threshold(R, 150, 255, cv.THRESH_BINARY)

    # merge the channels into original image
    merged_image = cv.merge([th_b, th_g, th_r])
    cv.imshow('merged', merged_image)

    cv.waitKey(0)


if __name__ == '__main__':
    main()
