import sys
import cv2
import dlib
import numpy
import matplotlib.pyplot as plt
from imutils import face_utils
import matplotlib.pyplot as plt

from utils.Camera import Camera, CameraType


def euclidean_distance(pointA, pointB):

    # Compute and return the euclidean distances between the 2 points
    return numpy.linalg.norm(pointA - pointB)


def eye_aspect_ratio(eye):

    # Compute the euclidean distances between 2 sets of vertical eye
    # landmarks (x,y) coordinate
    A = euclidean_distance(eye[1], eye[5])
    B = euclidean_distance(eye[2], eye[4])

    # Compute the euclidean distance between the horizontal eye landmark
    # (x, y) coordinate
    C = euclidean_distance(eye[0], eye[3])

    # Compute the eye aspect ratio
    ear = (A + B) / (2.0 * C)

    # Return the eye aspect ratio
    return ear


plt.style.use("ggplot")

def live_plotter(x_vec, y1_data, line1, identifier='', pause_time=0.1):
    if line1 == []:
        plt.ion()
        fig = plt.figure(figsize=(13, 6))
        ax = fig.add_subplot(111)
        line1, = ax.plot(x_vec, y1_data, '-o', alpha=0.8)
        plt.ylabel("Y Label")
        plt.title("Title: {}".format(identifier))
        plt.show()

    line1.set_ydata(y1_data)

    if numpy.min(y1_data) <= line1.axes.get_ylim()[0] or numpy.max(y1_data) >= line1.axes.get_ylim()[1]:
        plt.ylim([numpy.min(y1_data) - numpy.std(y1_data), numpy.max(y1_data) + numpy.std(y1_data)])

    plt.pause(pause_time)

    return line1

predictor_path = sys.argv[1]

camera = Camera(CameraType.WEB_CAM)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)

window = dlib.image_window()
window.set_title("Face Detector")

line1 = []
x_vec = numpy.linspace(0, 1, 101)[0 : -1]
y_vec = [0] * len(x_vec)

while True:
    frame = camera.take_frame()

    dets = detector(frame)

    window.set_image(frame)
    window.clear_overlay()
    window.add_overlay(dets)

    for k, d in enumerate(dets):

        shape = predictor(frame, d)

        window.add_overlay(shape)

        np_shape = face_utils.shape_to_np(shape)
        (leftStart, leftEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
        (rightStart, rightEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

        leftEye = np_shape[leftStart: leftEnd]
        rightEye = np_shape[rightStart: rightEnd]

        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)

        average_EAR = (leftEAR + rightEAR) / 2.0

        # print("Left EAR: {0:.3f} Right EAR: {0:.3f} Average EAR: {0:.3f}".format(
        #     leftEAR, rightEAR, average_EAR))

        # Plot EAR using console
        # value = int(average_EAR * 100)
        # for i in range(value):
        #     print("*", end='')
        # print("")

        # Plot EAR using matplotlib
        y_vec[-1] = average_EAR
        line1 = live_plotter(x_vec, y_vec, line1)
        y_vec = numpy.append(y_vec[1:], 0.0)

            
