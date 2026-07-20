import os

from logger import logger


class CandidateLoader:

    @staticmethod
    def load(
        folder_path
    ):

        resumes = []

        for file in os.listdir(
            folder_path
        ):

            if file.lower().endswith(

                (
                    ".pdf",
                    ".docx",
                    ".png",
                    ".jpg",
                    ".jpeg"
                )

            ):

                resumes.append(

                    os.path.join(
                        folder_path,
                        file
                    )

                )

        logger.info(
            f"{len(resumes)} resumes loaded"
        )

        return resumes