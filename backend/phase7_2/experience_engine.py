from logger import logger

from phase7_2.experience_matcher import (
    ExperienceMatcher
)

from phase7_2.experience_scorer import (
    ExperienceScorer
)


class ExperienceEngine:

    def analyze(

        self,

        resume_profile,
        jd_profile

    ):

        experiences = (

            resume_profile
            .get(

                "experience_details",

                []

            )

        )

        result = (

            ExperienceMatcher
            .match(

                experiences,

                jd_profile[
                    "skills"
                ]

            )

        )

        experience_score = (

            ExperienceScorer
            .score(

                result[
                    "scores"
                ]

            )

        )

        logger.info(
            "Experience relevance analysis completed"
        )

        return {

            "experience_relevance":

                experience_score,

            "relevant_experience":

                result[
                    "relevant_experience"
                ]
        }