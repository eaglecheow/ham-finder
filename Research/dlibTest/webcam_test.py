import cv2
import dlib
import sys

predictor_path = sys.argv[1]

# cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

window = dlib.image_window()
window.set_title("dlib Image")

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)

while rval:
    # cv2.imshow("preview", frame)
    rval, frame = vc.read()

    img = frame

    dets = detector(img, 1)

    window.clear_overlay()

    for k, d in enumerate(dets):
        shape = predictor(img, d)
        window.add_overlay(shape)

    window.set_image(img)
    window.add_overlay(dets)