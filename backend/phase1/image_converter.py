from pdf2image import convert_from_path


class ImageConverter:

    @staticmethod
    def pdf_to_images(pdf_path):

        images = convert_from_path(
            pdf_path
        )

        return images