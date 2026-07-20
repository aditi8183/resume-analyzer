from logger import logger


class ScoreCalculator:

    @staticmethod
    def calculate(

        skill_score,
        keyword_score,
        experience_gap,
        critical_missing_count=0,

        education_score=0,
        certification_score=0

    ):

        # ---------------------
        # Experience Score
        # ---------------------

        if experience_gap <= 0:

            experience_score = 100

        elif experience_gap == 1:

            experience_score = 80

        elif experience_gap == 2:

            experience_score = 60

        else:

            experience_score = 40

        # ---------------------
        # ATS Score
        # ---------------------

        ats_score = round(

            (

                skill_score * 0.50

            )

            +

            (

                keyword_score * 0.10

            )

            +

            (

                experience_score * 0.25

            )

            +

            (

                education_score * 0.10

            )

            +

            (

                certification_score * 0.05

            ),

            2

        )

        # ---------------------
        # Critical Skill Penalty
        # ---------------------
        print(
            "CRITICAL MISSING:",
               critical_missing_count
        )
        
             
        penalty = min(

            critical_missing_count * 8,
            25

        )
        print(
            "PENALTY:",
              penalty
        )

        ats_score = max(

            ats_score - penalty,

            0

        )

        # ---------------------
        # Fit Level
        # ---------------------

        if ats_score >= 80:

            fit_level = "Excellent Match"

        elif ats_score >= 65:

            fit_level = "Good Match"

        elif ats_score >= 45:

            fit_level = "Average Match"

        else:

            fit_level = "Poor Match"

        logger.info(
            "ATS score calculated"
        )

        return {

            "ats_score":
                ats_score,

            "skill_score":
                skill_score,

            "keyword_score":
                keyword_score,

            "experience_score":
                experience_score,

            "education_score":
                education_score,

            "certification_score":
                certification_score,

            "fit_level":
                fit_level
        }