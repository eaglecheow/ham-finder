"""
This code supposingly detect the the degree of movement for the face.
Possible use case is to additionally check if face is moving around
or just dead still.
"""

import sys
from enum import Enum
import dlib
from imutils import face_utils

from utils.Camera import Camera, CameraType
from utils.GraphPlotter import GraphPlotter
from utils.ImageTools import ImageTools

class FacePart(Enum):
    MOUTH = "mouth"
    INNER_MOUTH = "inner_mouth"
    RIGHT_EYEBROW = "right_eyebrow"
    LEFT_EYEBROW = "left_eyebrow"
    RIGHT_EYE = "right_eye"
    LEFT_EYE = "left_eye"
    NOSE = "nose"
    JAW = "jaw"

predictor_path = sys.argv[1]

is_video_mode = False
video_path = ""
if len(sys.argv) > 2:
    is_video_mode = True
    video_path = sys.argv[2]

camera = Camera(CameraType.WEB_CAM)

if is_video_mode:
    camera = Camera(CameraType.VIDEO, video_path)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)
plotter = GraphPlotter()
window = dlib.image_window()

window.set_title("Face Detector")

while True:

    frame = camera.take_frame()

    dets = detector(frame)