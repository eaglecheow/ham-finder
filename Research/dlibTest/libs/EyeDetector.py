import numpy

class EyeDetector:
    
    def euclidean_distance(self, pointA, pointB):

        # Compute and return the euclidean distances between the 2 points
        return numpy.linalg.norm(pointA - pointB)

    def eye_aspect_ratio(self, eye):

        # Compute the euclidean distances between 2 sets of vertical eye
        # landmarks (x,y) coordinate
        A = self.euclidean_distance(eye[1], eye[5])
        B = self.euclidean_distance(eye[2], eye[4])

        # Compute the euclidean distance between the horizontal eye landmark
        # (x, y) coordinate
        C = self.euclidean_distance(eye[0], eye[3])

        # Compute the eye aspect ratio
        ear = (A + B) / (2.0 * C)

        # Return the eye aspect ratio
        return ear

