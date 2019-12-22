from utils.Camera import Camera, CameraType
import numpy as np
import dlib
import cv2
import time


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

    print(kp1)

    outputImage = cv2.drawMatches(previousImage, kp1, currentImage, kp2, matches, None, flags=2)

    imageWindow.set_image(outputImage)

    previousImage = currentImage

    # time.sleep(1)

