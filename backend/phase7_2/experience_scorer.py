from logger import logger


class ExperienceScorer:

    @staticmethod
    def score(

        experience_scores

    ):

        if len(
            experience_scores
        ) == 0:

            return 0

        score = round(

            (
                sum(
                    experience_scores
                )

                /

                len(
                    experience_scores
                )
            )

            * 100,

            2

        )

        logger.info(
            "Experience score calculated"
        )

        return score