from logger import logger


class JobLevelDetector:

    @staticmethod
    def detect(
        experience
    ):

        if experience <= 2:

            level = "Junior"

        elif experience <= 5:

            level = "Mid"

        else:

            level = "Senior"

        logger.info(
            "Job level detected"
        )

        return level
