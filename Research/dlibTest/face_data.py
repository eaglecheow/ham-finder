import sys
import cv2
import dlib
import numpy
from imutils import face_utils

from utils.Camera import Camera, CameraType

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