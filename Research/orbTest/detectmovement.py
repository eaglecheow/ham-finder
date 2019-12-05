from utils.Camera import Camera, CameraType
from utils.GraphPlotter import GraphPlotter

import numpy as np
import dlib
import cv2
import time

import math


camera = Camera(CameraType.WEB_CAM)
orb = cv2.ORB_create()
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

faceDetector = dlib.get_frontal_face_detector()

imageWindow = dlib.image_window()
gp = GraphPlotter(yRange=[0, 100])
gp.add_plot("dmatch-mean")
gp.add_plot("real-mean")

previousImage = camera.take_frame()
previousDetectedFaceList = faceDetector(previousImage)

while True:

    currentImage = camera.take_frame()
    currentDetectedFaceList = faceDetector(currentImage)

    kp1, des1 = orb.detectAndCompute(previousImage, None)
    kp2, des2 = orb.detectAndCompute(currentImage, None)

    try:
        matches = bf.match(des1, des2)
    except:
        print("Something happened...")
        continue

    matches = sorted(matches, key=lambda x:x.distance)

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

        includeKeypoint = True

        for faceIndex, faceBoundingBox in enumerate(previousDetectedFaceList):
            if (
                (image1Coordinate[0] > faceBoundingBox.left()) and 
                (image1Coordinate[0] < faceBoundingBox.right()) and
                (image1Coordinate[1] > faceBoundingBox.top()) and
                (image1Coordinate[1] < faceBoundingBox.bottom())):
                includeKeypoint = False

        for faceIndex, faceBoundingBox in enumerate(currentDetectedFaceList):
            if (
                (image2Coordinate[0] > faceBoundingBox.left()) and 
                (image2Coordinate[0] < faceBoundingBox.right()) and
                (image2Coordinate[1] > faceBoundingBox.top()) and
                (image2Coordinate[1] < faceBoundingBox.bottom())):
                includeKeypoint = False


        if includeKeypoint == False:
            continue

        xDiff = abs(image1Coordinate[0] - image2Coordinate[0])
        yDiff = abs(image1Coordinate[1] - image2Coordinate[1])

        dist = math.sqrt((xDiff * xDiff) + (yDiff * yDiff))

        if dist > 100:
            continue

        dmatchDistanceList.append(match.distance)
        realDistanceList.append(dist)

        cv2.line(outputImage, (int(image1Coordinate[0]), int(image1Coordinate[1])), (int(image2Coordinate[0]), int(image2Coordinate[1])), (0, 255, 0), 1)


    # print("DMatch mean: {}, Real mean: {}".format(np.mean(dmatchDistanceList), np.mean(realDistanceList)))
    gp.input_value("dmatch-mean", np.mean(dmatchDistanceList))
    gp.input_value("real-mean", np.mean(realDistanceList))

    imageWindow.clear_overlay()

    imageWindow.set_image(outputImage)
    imageWindow.add_overlay(currentDetectedFaceList)
    imageWindow.add_overlay(previousDetectedFaceList)

    previousImage = currentImage
    previousDetectedFaceList = currentDetectedFaceList