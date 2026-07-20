from logger import logger


class RankingEngine:

    @staticmethod
    def calculate(

        ats_score,
        semantic_score,
        fit_score,

        project_score=0,
        experience_relevance_score=0,

        education_score=0,
        certification_score=0,

        critical_missing_count=0,

        matched_skill_count=0,
        missing_skill_count=0

    ):

        final_score = (

            (fit_score * 0.25)

            +

            (ats_score * 0.15)

            +

            (semantic_score * 0.15)

            +

            (project_score * 0.15)

            +

            (experience_relevance_score * 0.15)

            +

            (education_score * 0.05)

            +

            (certification_score * 0.05)

        )

        # Bonus for matching skills
        final_score += matched_skill_count * 1.5

        # Penalty for missing skills
        final_score -= missing_skill_count * 0.5

        # Heavy penalty for critical skills
        final_score -= critical_missing_count * 8

        final_score = max(

            final_score,

            0

        )

        logger.info(
            "Ranking score calculated"
        )

        return round(
            final_score,
            2
        )