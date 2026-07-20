from logger import logger


class ProjectScorer:

    @staticmethod
    def score(

        project_scores

    ):

        if len(
            project_scores
        ) == 0:

            return 0

        score = round(

            (
                sum(
                    project_scores
                )

                /

                len(
                    project_scores
                )
            )

            * 100,

            2

        )

        logger.info(
            "Project score calculated"
        )

        return score