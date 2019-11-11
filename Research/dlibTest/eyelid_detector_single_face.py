"""
This code supposingly limits the face detector to only capture a single face
from the camera. Phasing out the possibility that information of other faces are
mixed in.
"""

import sys
import dlib
from imutils import face_utils
import time

from utils.Camera import Camera, CameraType
from utils.DataCalculator import DataCalculator
from libs.EyeDetector import EyeDetector
from utils.GraphPlotter import GraphPlotter
from utils.ImageTools import ImageTools


VARIANCE25_THRESHOLD = 0.025
MAX_IDLE_FRAME = 200
MAX_IDLE_TIME = 10 # Maximum idle time to trigger in seconds


# System arguments
predictor_path = sys.argv[1]

# Check if code running in video mode
is_video_mode = False
video_path = ""
if len(sys.argv) > 2:
    is_video_mode = True
    video_path = sys.argv[2]

# Define class objects
camera = Camera(CameraType.WEB_CAM)

# Convert into video mode if enabled
if is_video_mode:
    camera = Camera(CameraType.VIDEO, video_path)

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


idle_counter = 0
is_idle = False
accumulated_idle_time = 0

previous_time = time.time()
current_time = time.time()

time.sleep(1)

while True:

    # Calculate time difference from previous frame
    previous_time = current_time
    current_time = time.time()
    period = current_time - previous_time

    # Takes the current frame from camera
    frame = camera.take_frame()

    dets = detector(frame)
    window.clear_overlay()
    window.set_image(frame)


    # Select the closest face in the frame
    max_face_area = 0
    selected_face = None

    # Skip loop if no face is detected
    if len(dets) <= 0:
        continue

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

    if variance25 > VARIANCE25_THRESHOLD:
        accumulated_idle_time = 0
    else:
        accumulated_idle_time = accumulated_idle_time + period

    if accumulated_idle_time > MAX_IDLE_TIME:
        frame = ImageTools.add_text_to_image(frame, "Idle detected")
        
        # Set image to the image window
        window.set_image(frame)

    

    # Plot the values
    plotter.input_value("average_ear", average_EAR)
    plotter.input_value("variance25", variance25)

