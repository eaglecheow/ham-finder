import sys
import cv2
import dlib
import numpy
import matplotlib.pyplot as plt
from imutils import face_utils

from utils.Camera import Camera, CameraType


def euclidean_distance(pointA, pointB):

    # Compute and return the euclidean distances between the 2 points
    return numpy.linalg.norm(pointA - pointB)


def eye_aspect_ratio(eye):

    # Compute the euclidean distances between 2 sets of vertical eye
    # landmarks (x,y) coordinate
    A = euclidean_distance(eye[1], eye[5])
    B = euclidean_distance(eye[2], eye[4])

    # Compute the euclidean distance between the horizontal eye landmark
    # (x, y) coordinate
    C = euclidean_distance(eye[0], eye[3])

    # Compute the eye aspect ratio
    ear = (A + B) / (2.0 * C)

    # Return the eye aspect ratio
    return ear


predictor_path = sys.argv[1]

camera = Camera(CameraType.WEB_CAM)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)

window = dlib.image_window()
window.set_title("Face Detector")

while True:
    frame = camera.take_frame()

    dets = detector(frame)

    window.set_image(frame)
    window.clear_overlay()
    window.add_overlay(dets)

    for k, d in enumerate(dets):

        shape = predictor(frame, d)

        window.add_overlay(shape)

        np_shape = face_utils.shape_to_np(shape)
        (leftStart, leftEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
        (rightStart, rightEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

        leftEye = np_shape[leftStart: leftEnd]
        rightEye = np_shape[rightStart: rightEnd]

        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)

        average_EAR = (leftEAR + rightEAR) / 2.0

        # print("Left EAR: {0:.3f} Right EAR: {0:.3f} Average EAR: {0:.3f}".format(
        #     leftEAR, rightEAR, average_EAR))

        value = int(average_EAR * 100)
        for i in range(value):
            print("*", end='')
        print("")

            
