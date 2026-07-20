from paddleocr import PaddleOCR


class OCRExtractor:

    def __init__(self):

        self.ocr = PaddleOCR(
            use_angle_cls=True,
            lang="en"
        )

    def extract(self, image):

        result = self.ocr.ocr(
            image,
            cls=True
        )

        return result[0] if result else []