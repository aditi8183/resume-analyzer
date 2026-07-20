from logger import logger


class RecommendationEngine:

    @staticmethod
    def generate(

        missing_skills,
        critical_missing,
        experience_gap

    ):

        recommendations = []

        for skill in critical_missing:

            recommendations.append(

                f"Critical skill missing: {skill}"

            )

        for skill in missing_skills:

            if skill not in critical_missing:

                recommendations.append(

                    f"Optional skill missing: {skill}"

                )

        if experience_gap > 0:

            recommendations.append(

                f"Need approximately {experience_gap} more years of experience"

            )

        logger.info(
            "Recommendations generated"
        )

        return recommendations