from utils.Camera import Camera, CameraType
import numpy as np
import dlib
import cv2
import time

import math


camera = Camera(CameraType.WEB_CAM)
orb = cv2.ORB_create()
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
imageWindow = dlib.image_window()

previousImage = camera.take_frame()

while True:

    currentImage = camera.take_frame()

    kp1, des1 = orb.detectAndCompute(previousImage, None)
    kp2, des2 = orb.detectAndCompute(currentImage, None)

    matches = bf.match(des1, des2)

    matches = sorted(matches, key=lambda x:x.distance)

    outputImage = currentImage

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

        print("{}:{}".format(match.distance, dist))

        # print("Coordinate --> Image1: [{}, {}], Image2: [{}, {}]".format(image1Coordinate[0], image1Coordinate[1], image2Coordinate[0], image2Coordinate[1]))

        cv2.line(outputImage, (int(image1Coordinate[0]), int(image1Coordinate[1])), (int(image2Coordinate[0]), int(image2Coordinate[1])), (0, 255, 0), 1)


    imageWindow.set_image(outputImage)

    previousImage = currentImage