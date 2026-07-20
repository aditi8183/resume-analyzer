from logger import logger


class FitPredictor:

    @staticmethod
    def predict(

        ats_score,
        semantic_score,
        project_score,
        experience_score

    ):

        fit_score = round(

            (

                ats_score * 0.25

            )

            +

            (

                semantic_score * 0.30

            )

            +

            (

                project_score * 0.25

            )

            +

            (

                experience_score * 0.20

            ),

            2

        )

        if fit_score >= 80:

            fit = "Excellent"

        elif fit_score >= 65:

            fit = "Good"

        elif fit_score >= 45:

            fit = "Average"

        else:

            fit = "Poor"

        logger.info(
            "Candidate fit predicted"
        )

        return {

            "fit_score":
                fit_score,

            "fit":
                fit
        }