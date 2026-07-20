from logger import logger


class ExplainabilityEngine:

    @staticmethod
    def generate(

        phase4_result,
        semantic_result

    ):

        strengths = []

        weaknesses = []

        recommendations = []

        scores = phase4_result["scores"]
        gaps = phase4_result["gaps"]

        if scores["skill_score"] >= 80:

            strengths.append(
                "Strong skill alignment"
            )

        if semantic_result["semantic_score"] >= 80:

            strengths.append(
                "Strong semantic relevance"
            )

        if semantic_result.get(
            "project_score",
            0
        ) >= 70:

            strengths.append(
                "Relevant project experience"
            )

        if semantic_result.get(
            "experience_relevance_score",
            0
        ) >= 70:

            strengths.append(
                "Relevant work experience"
            )

        if gaps["missing_skills"]:

            weaknesses.append(

                "Missing skills: "

                +

                ", ".join(

                    gaps[
                        "missing_skills"
                    ][:5]

                )

            )

        if gaps["experience_gap"] > 0:

            weaknesses.append(

                f"Experience gap: "

                f"{gaps['experience_gap']} years"

            )

        if scores["ats_score"] >= 80:

            recommendations.append(
                "Highly recommended for interview"
            )

        elif scores["ats_score"] >= 65:

            recommendations.append(
                "Recommended for screening round"
            )

        else:

            recommendations.append(
                "Needs further review"
            )

        logger.info(
            "Explainability generated"
        )

        return {

            "strengths":
                strengths,

            "weaknesses":
                weaknesses,

            "recommendations":
                recommendations
        }