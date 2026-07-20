from logger import logger

from phase6.semantic_matcher import (
    SemanticMatcher
)


class ExperienceMatcher:

    THRESHOLD = 0.50

    IMPACT_KEYWORDS = [

        "improved",
        "increased",
        "reduced",
        "optimized",
        "automated",
        "achieved",
        "delivered",
        "saved",
        "generated",
        "boosted",
        "enhanced",
        "decreased"
    ]

    LEADERSHIP_KEYWORDS = [

        "led",
        "managed",
        "mentored",
        "supervised",
        "owned",
        "coordinated",
        "headed",
        "directed"
    ]

    @staticmethod
    def match(

        experiences,
        jd_skills

    ):

        relevant_experience = []

        experience_scores = []

        impact_score = 0

        leadership_score = 0

        for experience in experiences:

            best_score = 0

            for skill in jd_skills:

                score = (

                    SemanticMatcher
                    .similarity(

                        experience,
                        skill

                    )

                )

                if score > best_score:

                    best_score = score

            experience_scores.append(
                best_score
            )

            if best_score >= (

                ExperienceMatcher
                .THRESHOLD

            ):

                relevant_experience.append(
                    experience
                )

            lower_exp = experience.lower()

            for keyword in (

                ExperienceMatcher
                .IMPACT_KEYWORDS

            ):

                if keyword in lower_exp:

                    impact_score += 5

            for keyword in (

                ExperienceMatcher
                .LEADERSHIP_KEYWORDS

            ):

                if keyword in lower_exp:

                    leadership_score += 5

        relevance_score = 0

        if len(experience_scores) > 0:

            relevance_score = (

                sum(experience_scores)

                /

                len(experience_scores)

            ) * 100

        experience_relevance_score = round(

            min(

                (

                    relevance_score * 0.7

                )

                +

                (

                    impact_score * 0.2

                )

                +

                (

                    leadership_score * 0.1

                ),

                100

            ),

            2

        )

        logger.info(
            "Experience matching completed"
        )

        return {

            "relevant_experience":
                relevant_experience,

            "scores":
                experience_scores,

            "impact_score":
                impact_score,

            "leadership_score":
                leadership_score,

            "experience_relevance_score":
                experience_relevance_score
        }