import cv2
from enum import Enum

class CameraType(Enum):
    WEB_CAM = 1
    PI_CAM = 2

class Camera:

    def __init__(self, cameraMode: CameraType):
        super().__init__()

        self.cameraMode = cameraMode

        if cameraMode == CameraType.WEB_CAM:
            print("[Camera] Initializing camera in mode: WEB_CAM")

            self.cameraObject = cv2.VideoCapture(0)

        elif cameraMode == CameraType.PI_CAM:
            print("[Camera] Initializing camera in mode: PI_CAM")

            raise NotImplementedError()

        else:
            print("[Camera] Camera mode does not exist")
            print("[Camera] Exiting program...")
            exit()

    
    def takeFrame(self):
        
        if self.cameraMode == CameraType.WEB_CAM:
            if self.cameraObject.isOpened():
                _, frame = self.cameraObject.read()
                return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            else:
                raise Exception("[Camera] Camera is not opened")
        elif self.cameraMode == CameraType.PI_CAM:
            raise NotImplementedError()