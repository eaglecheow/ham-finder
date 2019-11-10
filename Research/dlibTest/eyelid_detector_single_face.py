"""
This code supposingly limits the face detector to only capture a single face
from the camera. Phasing out the possibility that information of other faces are
mixed in.
"""

import sys
import dlib
from imutils import face_utils

from utils.Camera import Camera, CameraType
from utils.DataCalculator import DataCalculator
from libs.EyeDetector import EyeDetector
from utils.GraphPlotter import GraphPlotter

# System arguments
predictor_path = sys.argv[1]

# Define class objects
camera = Camera(CameraType.WEB_CAM)
eye_detector = EyeDetector()
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)
plotter = GraphPlotter()
window = dlib.image_window()

window.set_title("Face detector")

# Calulates data with small sample size
data_calculator = DataCalculator(dataSize=5)

# Calculates data with big sample size
data_calculator_mean = DataCalculator(dataSize=50)

# Define what data to plot
plotter.add_plot("average_ear", "Average EAR")
plotter.add_plot("variance25", "Variance x25")

while True:

    # Takes the current frame from camera
    frame = camera.take_frame()

    dets = detector(frame)

    window.set_image(frame)
    window.clear_overlay()



    # Select the closest face in the frame
    max_face_area = 0
    selected_face = None

    for k, d in enumerate(dets):

        x_diff = abs(d.right() - d.left())
        y_diff = abs(d.bottom() - d.top())

        face_area = x_diff * y_diff

        if face_area > max_face_area:
            max_face_area = face_area
            selected_face = d

    # Get face feature for the seleted face
    shape = predictor(frame, selected_face)
    
    window.add_overlay(d)
    window.add_overlay(shape)

    np_shape = face_utils.shape_to_np(shape)
    (left_start, left_end) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
    (right_start, right_end) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

    left_eye = np_shape[left_start : left_end]
    right_eye = np_shape[right_start : right_end]

    left_EAR = eye_detector.eye_aspect_ratio(left_eye)
    right_EAR = eye_detector.eye_aspect_ratio(right_eye)

    average_EAR = (left_EAR + right_EAR) / 2.0

    data_calculator.input_value(average_EAR)
    data_calculator_mean.input_value(average_EAR)
    
    variance25 = data_calculator.variance_value * 25

    # Plot the values
    plotter.input_value("average_ear", average_EAR)
    plotter.input_value("variance25", variance25)
