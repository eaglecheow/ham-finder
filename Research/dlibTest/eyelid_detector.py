import sys
import cv2
import dlib
import numpy
from imutils import face_utils

from utils.Camera import Camera, CameraType
from utils.DataCalculator import DataCalculator
from libs.EyeDetector import EyeDetector
from utils.GraphPlotter import GraphPlotter

predictor_path = sys.argv[1]

camera = Camera(CameraType.WEB_CAM)
eye_detector = EyeDetector()
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)

data_calculator = DataCalculator(dataSize=5)
data_calculator_median = DataCalculator(dataSize=50)

window = dlib.image_window()
window.set_title("Face Detector")

g_plotter = GraphPlotter()
g_plotter.add_plot("ear")
g_plotter.add_plot("std")
g_plotter.add_plot("median")
g_plotter.add_plot("is_eye_open")
# g_plotter.add_plot("action_level")

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

        leftEAR = eye_detector.eye_aspect_ratio(leftEye)
        rightEAR = eye_detector.eye_aspect_ratio(rightEye)

        average_EAR = (leftEAR + rightEAR) / 2.0

        data_calculator.input_value(average_EAR)
        data_calculator_median.input_value(average_EAR)

        # action_level = 0
        # if data_calculator.sd_value >= 0.025:
        #     action_level = 0.4
        # else:
        #     action_level = 0

        is_eye_open = 0
        if average_EAR >= 0.25:
            is_eye_open = 0.4

        g_plotter.input_value("ear", average_EAR)
        g_plotter.input_value("std", data_calculator.sd_value)
        g_plotter.input_value("median", data_calculator_median.median_value)
        g_plotter.input_value("is_eye_open", is_eye_open)
        # g_plotter.input_value("action_level", action_level)

            
