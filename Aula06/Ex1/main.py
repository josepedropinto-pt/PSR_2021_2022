#!/usr/bin/env python

import cv2 as cv
import numpy as np


def main():

    # import the original image
    original_image = cv.imread('../../Aula5/Ex2/atlascar.png', 1)

    # Extract tuple of shape parameters
    (w, h, ch) = original_image.shape

    # Define circle function parameters
    centroid = (int(h / 2), int(w / 2))
    print(str(centroid))
    green_color = (0, 255, 0)
    thickness = 2
    radius = 40

    # Define put_text function parameters
    text = 'This is PSR, RUN while you can..'
    coord = (50, 50)
    text_color = (0, 0, 255)
    text_thickness = 5

    # Plot circle and image
    cv.circle(original_image, centroid, radius, green_color, thickness)
    cv.putText(original_image, text, coord,cv.FONT_HERSHEY_SIMPLEX, 1, text_color, text_thickness)
    cv.imshow('original image', original_image)

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
