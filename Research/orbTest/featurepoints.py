from utils.Camera import Camera, CameraType
import cv2
from matplotlib import pyplot as plt
import dlib

camera = Camera(CameraType.WEB_CAM)
orb = cv2.ORB_create()
imageWindow = dlib.image_window()

while True:

    frame = camera.take_frame()

    keypoint = orb.detect(frame, None)

    keypoint, descriptors = orb.compute(frame, keypoint)

    outputImage = cv2.drawKeypoints(frame, keypoint, cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS, color=(0, 255, 0), flags=0)

    imageWindow.set_image(outputImage)

