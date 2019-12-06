from data import constants
from detection.utils.Camera import Camera, CameraType
from detection.face_detection.EyelidDetector import EyelidDetector


class AccidentDetector:
    def __init__(self):
        super().__init__()

        self.camera = Camera(CameraType.WEB_CAM)
        self.eyelidDetector = EyelidDetector(
            constants.PREDICTION_FILE_PATH, self.camera
        )

    def performDetection(self):

        eyelidDetectionResults = self.eyelidDetector.frameDetection()
        

