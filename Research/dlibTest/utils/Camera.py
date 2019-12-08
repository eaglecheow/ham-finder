import cv2
from enum import Enum

class CameraType(Enum):
    WEB_CAM = 1
    PI_CAM = 2


class Camera:

    def __init__(self, mode: CameraType):

        self.mode = mode
        # self.is_camera_open = False

        if mode == CameraType.WEB_CAM:
            print("[Camera] Initializing camera in mode: WEB_CAM")

            # Initialize Webcam
            self.camera_object = cv2.VideoCapture(0)

            # if self.camera_object.isOpened():
            #     self.is_camera_open, frame = self.camera_object.read()
            # else:
            #     self.is_camera_open = False;

        elif mode == CameraType.PI_CAM:
            # TODO: Initialize Pi Cam
            print("[Camera] Initializing camera in mode: PI_CAM")
            raise Exception("Not Implemented")

        else:
            print("[Camera] Camera mode does not exist")
            print("[Camera] Exiting program...")
            exit()


    def take_frame(self):

        if (self.mode == CameraType.WEB_CAM):
            if self.camera_object.isOpened():
                _, frame = self.camera_object.read()
                return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            else:
                raise Exception("[Camera] Camera is not open")
        elif (self.mode == CameraType.PI_CAM):
            raise Exception("Not Implemented")