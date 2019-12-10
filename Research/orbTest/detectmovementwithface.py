from utils.Camera import Camera, CameraType
from utils.GraphPlotter import GraphPlotter

import numpy as np
import dlib
import cv2
import time

import math

NOISE_FILTER_MARGIN = 75

camera = Camera(CameraType.WEB_CAM)
orb = cv2.ORB_create()
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
faceDetector = dlib.get_frontal_face_detector()

imageWindow = dlib.image_window()
gp = GraphPlotter(yRange=[0, 100])
gp.add_plot("dmatch-mean")
gp.add_plot("real-mean")

previousImage = camera.take_frame()

while True:

    currentImage = camera.take_frame()

    kp1, des1 = orb.detectAndCompute(previousImage, None)
    kp2, des2 = orb.detectAndCompute(currentImage, None)

    try:
        matches = bf.match(des1, des2)
    except:
        print("Something happened...")
        continue

    matches = sorted(matches, key=lambda x: x.distance)

    outputImage = currentImage

    dmatchDistanceList = []
    realDistanceList = []

    for match in matches:

        image1KeypointId = match.queryIdx
        image2KeypointId = match.trainIdx

        image1Keypoint = kp1[image1KeypointId]
        image2Keypoint = kp2[image2KeypointId]

        image1Coordinate = image1Keypoint.pt
        image2Coordinate = image2Keypoint.pt

        xDiff = abs(image1Coordinate[0] - image2Coordinate[0])
        yDiff = abs(image1Coordinate[1] - image2Coordinate[1])

        dist = math.sqrt((xDiff * xDiff) + (yDiff * yDiff))

        if dist > NOISE_FILTER_MARGIN:
            continue

        dmatchDistanceList.append(match.distance)
        realDistanceList.append(dist)

        cv2.line(
            outputImage,
            (int(image1Coordinate[0]), int(image1Coordinate[1])),
            (int(image2Coordinate[0]), int(image2Coordinate[1])),
            (0, 255, 0),
            1,
        )

    gp.input_value("dmatch-mean", np.mean(dmatchDistanceList))
    gp.input_value("real-mean", np.mean(realDistanceList))

    imageWindow.clear_overlay()

    imageWindow.set_image(outputImage)

    previousImage = currentImage
