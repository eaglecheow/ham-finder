import cv2

class ImageTools:

    @staticmethod
    def add_text_to_image(image, text: str, colorRGB=(0, 0, 255)):
        return cv2.putText(image, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, colorRGB, 3)