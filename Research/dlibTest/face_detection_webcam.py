'''
For this script, please specifically use [shape_predictor_68_face_landmarks.dat] for trained model
'''

import sys
import cv2
import dlib

from imutils import face_utils

from utils.Camera import Camera, CameraType


predictor_path = sys.argv[1]

if len(sys.argv) < 1:
    print("[Init] Please include trained model")
    exit()

window = dlib.image_window()
window.set_title("Test Video")

detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor(predictor_path)

camera = Camera(CameraType.WEB_CAM)
while True:
    image = camera.take_frame()

    dets = detector(image)

    window.clear_overlay()

    for k, d in enumerate(dets):
        shape = shape_predictor(image, d)

        new_shape = face_utils.shape_to_np(shape)
        (leftStart, leftEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
        (rightStart, rightEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

        leftEye = new_shape[leftStart:leftEnd]
        rightEye = new_shape[rightStart:rightEnd]

        print("===")
        print("Left Eye: {}".format(leftEye))
        print("Right Eye: {}".format(rightEye))
        print("===")

        window.add_overlay(shape)

    
    window.add_overlay(dets)

    window.set_image(image)
