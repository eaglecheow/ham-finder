import sys
from detection.utils.Camera import Camera, CameraType
from detection.face_detection.EyelidDetector import EyelidDetector

predictionFilePath = sys.argv[1]

camera = Camera(CameraType.WEB_CAM)
eyelidDetector = EyelidDetector(
    predictionFilePath, 
    camera,
    eyelidMovementTimeout=5000,
    showFrame=True
)

while True:
    print("IsActive: {}".format(eyelidDetector.frameDetection()))
