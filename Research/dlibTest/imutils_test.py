import imutils
import dlib
import sys


img_path = sys.argv[1]

img = dlib.load_rgb_image(img_path)

# translated_image = imutils.translate(img, 30, 30)

# rotated_image = imutils.rotate(img, 90)

resized_image = imutils.resize(img, 100)

window = dlib.image_window()

window.set_image(resized_image)

dlib.hit_enter_to_continue()