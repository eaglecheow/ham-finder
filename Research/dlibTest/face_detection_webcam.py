'''
For this script, please specifically use [shape_predictor_68_face_landmarks.dat] for trained model
'''

import sys
import cv2
import dlib


class Camera:
    def __init__(self, mode):

        self.mode = mode
        self.is_camera_open = False

        if mode == "WEB_CAM":
            print("[Camera] Initializing camera in mode: WEB_CAM")

            # Initialize camera with webcam
            self.camera_object = cv2.VideoCapture(0)

            if self.camera_object.isOpened():
                self.is_camera_open, frame = self.camera_object.read()
            else:
                self.is_camera_open = False

        elif mode == "PI_CAM":
            print("[Camera] Initializing camera in mode: PI_CAM")

            # Initialize camera with Pi Camera
            raise Exception("Not Implemented")
        else:
            print("[Camera] Invalid camera mode")
            print("Exiting program...")
            exit()

    def take_frame(self):

        # If camera not open, throw exception
        if (self.is_camera_open == False):
            raise Exception("[Camera] Camera not open")

        # Grab a frame from the camera, and return as image
        if self.mode == "WEB_CAM":
            self.is_camera_open, image = self.camera_object.read()
            return cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
        elif self.mode == "PI_CAM":
            raise Exception("Not implemented")

predictor_path = sys.argv[1]

if len(sys.argv) < 1:
    print("[Init] Please include trained model")
    exit()

window = dlib.image_window()
window.set_title("Test Video")

detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor(predictor_path)

camera = Camera("WEB_CAM")
while True:
    image = camera.take_frame()

    dets = detector(image)

    window.clear_overlay()

    for k, d in enumerate(dets):
        shape = shape_predictor(image, d)
        window.add_overlay(shape)

    
    window.add_overlay(dets)

    window.set_image(image)
