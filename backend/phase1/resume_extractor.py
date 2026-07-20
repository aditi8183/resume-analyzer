import os

from phase1.pdf_extractor import (
    PDFExtractor
)

from phase1.image_converter import (
    ImageConverter
)

from phase1.ocr_extractor import (
    OCRExtractor
)

from phase1.confidence_scorer import (
    ConfidenceScorer
)

from phase1.garbage_detector import (
    GarbageDetector
)

from phase1.text_quality_checker import (
    TextQualityChecker
)

from logger import logger


class ResumeExtractor:

    def __init__(self):

        self.ocr = OCRExtractor()

    def extract(self, file_path):

        extension = os.path.splitext(
            file_path
        )[1].lower()

        # ===================================
        # PDF INPUT
        # ===================================

        if extension == ".pdf":

            try:
            

                pdf_data = PDFExtractor.extract(file_path)
                text = pdf_data["text"]
                blocks = pdf_data["blocks"]

                confidence = (
                    ConfidenceScorer
                    .pdf_confidence()
                )

                source = "pdf"

            except Exception:
                blocks = []
                images = (
                    ImageConverter
                    .pdf_to_images(
                        file_path
                    )
                )

                ocr_text = []

                confidences = []

                for image in images:

                    result = (
                        self.ocr.extract(
                            image
                        )
                    )

                    confidences.append(

                        ConfidenceScorer
                        .ocr_confidence(
                            result
                        )

                    )

                    for line in result:

                        try:

                            ocr_text.append(
                                line[1][0]
                            )

                        except Exception:
                            pass

                text = "\n".join(
                    ocr_text
                )

                confidence = round(

                    sum(confidences)
                    /
                    max(
                        len(confidences),
                        1
                    ),

                    4
                )

                source = "ocr"

        # ===================================
        # IMAGE INPUT
        # ===================================

        elif extension in [

            ".png",
            ".jpg",
            ".jpeg"

        ]:

            result = self.ocr.extract(
                file_path
            )

            confidence = (
                ConfidenceScorer
                .ocr_confidence(
                    result
                )
            )

            lines = []

            for line in result:

                try:

                    lines.append(
                        line[1][0]
                    )

                except Exception:
                    pass

            text = "\n".join(
                lines
            )

            source = "image"

        else:

            raise ValueError(
                f"Unsupported file type: {extension}"
            )

        # ===================================
        # CLEANING
        # ===================================

        cleaned_lines = []

        for line in text.split("\n"):

            if (
                GarbageDetector
                .is_garbage(line)
            ):
                continue

            if (
                not TextQualityChecker
                .is_valid_text(line)
            ):
                continue

            cleaned_lines.append(
                line.strip()
            )

        final_text = "\n".join(
            cleaned_lines
        )

        logger.info(
            "Resume extraction completed"
        )

        return {

            "source": source,

            "confidence":
                confidence,

            "text":
                final_text,
            
            "blocks":
                blocks
        }