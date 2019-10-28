import sys
import os
import dlib
import glob

if len(sys.argv) != 4:
    print(
        "Call this program like this:\n"
        "   ./face_recognition.py shape_predictor_5_face_landmarks.dat dlib_face_recognition_resnet_model_v1.dat ../examples/faces\n"
        "You can download a trained facial shape predictor and recognition model from:\n"
        "    http://dlib.net/files/shape_predictor_5_face_landmarks.dat.bz2\n"
        "    http://dlib.net/files/dlib_face_recognition_resnet_model_v1.dat.bz2"
    )

    exit()


predictor_path = sys.argv[1]
face_rec_model_path = sys.argv[2]
faces_folder_path = sys.argv[3]

detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor(predictor_path)
facerec = dlib.face_recognition_model_v1(face_rec_model_path)

win = dlib.image_window()

for f in glob.glob(os.path.join(faces_folder_path, "*.jpg")):
    print("Processing file: {}".format(f))
    img = dlib.load_rgb_image(f)

    win.clear_overlay()
    win.set_image(img)

    dets = detector(img, 1)
    print("Number of faces detected: {}".format(len(dets)))

    for k, d in enumerate(dets):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
            k, d.left(), d.top(), d.right(), d.bottom()
        ))
        shape = sp(img, d)
        win.clear_overlay()
        win.add_overlay(d)
        win.add_overlay(shape)

        face_descriptor = facerec.compute_face_descriptor(img, shape)
        print(face_descriptor)

        print("Computing descriptor on aligned image ...")

        face_chip = dlib.get_face_chip(img, shape)

        face_descriptor_from_prealigned_image = facerec.compute_face_descriptor(face_chip)
        print(face_descriptor_from_prealigned_image)

        dlib.hit_enter_to_continue()