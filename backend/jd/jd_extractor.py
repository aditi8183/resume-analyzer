# jd/jd_extractor.py

import os
import fitz


class JDExtractor:

    def extract(
        self,
        file_path
    ):

        extension = os.path.splitext(
            file_path
        )[1].lower()

        # -------------------------
        # TXT
        # -------------------------

        if extension == ".txt":

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:

                return file.read()

        # -------------------------
        # PDF
        # -------------------------

        elif extension == ".pdf":

            document = fitz.open(
                file_path
            )

            text = ""

            for page in document:

                text += (
                    page.get_text()
                    + "\n"
                )

            document.close()

            return text

        else:

            raise ValueError(

                f"Unsupported JD format: {extension}"

            )