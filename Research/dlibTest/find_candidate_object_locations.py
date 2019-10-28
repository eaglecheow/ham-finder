import sys
import dlib

image_file = sys.argv[1]
img = dlib.load_rgb_image(image_file)

# Location of candidate objects will be saved into rects
rects = []
dlib.find_candidate_object_locations(img, rects, min_size=500)

print("Number of rectangles found: {}".format(len(rects)))
for k, d in enumerate(rects):
    print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
        k, d.left(), d.top(), d.right(), d.bottom()
    ))