import sys
from face_detection.EyelidDetector import EyelidDetector

predictionFilePath = sys.argv[1]

eyelidDetector = EyelidDetector(predictionFilePath, eyelidMovementTimeout=10000, showFrame=True)

while True:
    isActive = eyelidDetector.frameDetection()

    print(isActive)