#!/usr/bin/env python
import timeit

import cv2 as cv
import mediapipe as mp
import time
from ttictoc import tic

# Initializing utils for drawing the facial landmarks on image
mpDraw = mp.solutions.drawing_utils

# Initializing utils for face mesh
mpFaceMesh = mp.solutions.face_mesh

# Face mesh with default confidence parameters
faceMesh = mpFaceMesh.FaceMesh()

# Personalize the print of the landmark points
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1,
                              color=(100, 100, 0))


def edgeDetection(Color_image, Gray_image):
    # Detect the edges with canny defining threshold
    edges_detected = cv.Canny(Gray_image, 80, 200)

    # Find the contours using the edges detected and draw them
    contours, hierarchy = cv.findContours \
        (edges_detected, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    cv.drawContours(Color_image, contours, -1, (0, 0, 255), 1)
    return Color_image


def main():
    # Start the capture
    capture = cv.VideoCapture(0)

    # Uses frontal face Cascade Classifier
    face_cascade = cv.CascadeClassifier(
        cv.data.haarcascades + "haarcascade_frontalface_default.xml")

    # Initialize time
    tic = time.time()
    while True:

        # Set the window name and configure it
        window_name = 'Ex2 Frame'
        cv.namedWindow(window_name, cv.WINDOW_GUI_EXPANDED)

        # Read the capture video and convert it to gray scale image
        _, frame = capture.read()
        cv.imshow('original', frame)
        gray_image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Face cascade function to detect the faces and store a tuple
        faces = face_cascade.detectMultiScale(gray_image, 1.3, 4)

        # new_frame = cv.cvtColor(frame, cv.COLOR_BGR2BGRA) Why??

        # Create copies from original image for overlays
        overlay_face = frame.copy()
        overlay_landmarks = frame.copy()
        overlay_lips = frame.copy()

        # Unpack the tuples and draw the rectangle on the image
        for (x, y, width, height) in faces:
            cv.rectangle(overlay_face, (x, y), (x + width, y + height),
                         (0, 180, 0), -1)

        # Make the "-1" fill of rect semi-transparent with alpha
        alpha = 0.35
        frame = cv.addWeighted(overlay_face, alpha, frame, 1 - alpha, 0)

        # Convert the landmarks overlay to RGB for processing
        frame2 = cv.cvtColor(overlay_landmarks, cv.COLOR_BGR2RGB)
        results = faceMesh.process(frame2)

        # If it detects any face into the results goes in
        if results.multi_face_landmarks:

            # Run all the elements of the results array
            for face in results.multi_face_landmarks:
                # Draw landmark points on the Overlay_landmarks
                mpDraw.draw_landmarks(overlay_landmarks, face,
                                      mpFaceMesh.FACEMESH_CONTOURS, drawSpec)

                # Get the (x,y) coordinates of landmark 13
                x_lip_up = results.multi_face_landmarks[0].landmark[13].x
                y_lip_up = results.multi_face_landmarks[0].landmark[13].y

                # Denormalize the values with respect to original image
                shape = overlay_lips.shape
                relative_x_lip_up = int(x_lip_up * shape[1])
                relative_y_lip_up = int(y_lip_up * shape[0])

                # Apply the same process for the landmark 14
                x_lip_down = results.multi_face_landmarks[0].landmark[14].x
                y_lip_down = results.multi_face_landmarks[0].landmark[14].y
                shape = overlay_lips.shape
                relative_x_lip_down = int(x_lip_down * shape[1])
                relative_y_lip_down = int(y_lip_down * shape[0])

                # Calculate the distances between the landmarks
                dist_x = relative_x_lip_up - relative_x_lip_down
                dist_y = abs(relative_y_lip_up - relative_y_lip_down)

            # Draw circle into the points chosen for the threshold
            cv.circle(frame, (relative_x_lip_up, relative_y_lip_up),
                      7, (255, 0, 0), thickness=-1)
            cv.circle(frame, (relative_x_lip_down, relative_y_lip_down),
                      7, (0, 0, 255), thickness=-1)

        # Threshold for the open and close mouse
        if dist_y >= 4:
            tic = time.time()
            speak = str('Someone is Speaking')
            cv.putText(overlay_lips, speak, (50, 50), cv.FONT_HERSHEY_SIMPLEX,
                       1, (0, 255, 0), 3)

        # Timing to avoid false positives
        elif time.time() - tic < 1:
            speak = str('Someone is Speaking')
            cv.putText(overlay_lips, speak, (50, 50), cv.FONT_HERSHEY_SIMPLEX,
                       1, (0, 255, 0), 3)
        else:
            no_speak = str('Nobody is speaking')
            cv.putText(overlay_lips, no_speak, (50, 50), cv.FONT_HERSHEY_SIMPLEX,
                       1, (0, 0, 255), 3)

        # Call function edge detect with the 2 required inputs
        edgeDetection(frame, gray_image)

        # Print a clean window with the Speaking challenge
        window_Lips = 'Speaking test'
        cv.namedWindow(window_Lips, cv.WINDOW_GUI_EXPANDED)
        cv.imshow(window_Lips, overlay_lips)

        # Plot the landmark points in another window
        window_LM = 'LandMark Points'
        cv.namedWindow(window_LM, cv.WINDOW_GUI_EXPANDED)
        cv.imshow(window_LM, overlay_landmarks)

        # Plot the frame with face detection and contours
        cv.imshow(window_name, frame)

        # Close the window and break with "q" press
        if cv.waitKey(1) == ord('q'):
            break

    # Release the camera and close the windows
    capture.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
