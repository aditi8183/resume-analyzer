import fitz


class PDFExtractor:

    @staticmethod
    def extract(pdf_path):

        document = fitz.open(pdf_path)

        text = ""
        blocks = []

        for page_num, page in enumerate(document):

            text += page.get_text() + "\n"

            page_blocks = page.get_text("blocks")

            for block in page_blocks:

                blocks.append(
                    {
                        "text": block[4].strip(),
                        "x0": block[0],
                        "y0": block[1],
                        "x1": block[2],
                        "y1": block[3],
                        "page": page_num + 1
                    }
                )

        document.close()

        return {
            "text": text.strip(),
            "blocks": blocks
        }