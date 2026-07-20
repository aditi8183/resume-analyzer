from logger import logger

from phase6.semantic_scorer import (
    SemanticScorer
)

from phase6.fit_predictor import (
    FitPredictor
)

from phase7_1.project_matcher import (
    ProjectMatcher
)

from phase7_2.experience_matcher import (
    ExperienceMatcher
)


class SemanticEngine:

    def analyze(

        self,

        resume_profile,
        jd_profile,
        phase4_result

    ):

        semantic_result = (

            SemanticScorer
            .score(

                resume_profile[
                    "skills"
                ],

                jd_profile[
                    "skills"
                ]

            )

        )
        print("SEMANTIC RESULT KEYS =", semantic_result.keys())
        print("SEMANTIC RESULT =", semantic_result)

        project_result = (

            ProjectMatcher
            .match(

                resume_profile.get(
                    "projects",
                    []
                ),

                jd_profile[
                    "skills"
                ]

            )

        )

        experience_result = (

            ExperienceMatcher
            .match(

                resume_profile.get(
                    "experience_details",
                    []
                ),

                jd_profile[
                    "skills"
                ]

            )

        )

        fit_result = (

            FitPredictor
            .predict(

                phase4_result[
                    "scores"
                ][
                    "ats_score"
                ],

                semantic_result[
                    "semantic_score"
                ],

                project_result[
                    "project_score"
                ],

                experience_result[
                    "experience_relevance_score"
                ]

            )

        )

        fit_score = fit_result[
            "fit_score"
        ]

        if fit_score >= 75:

            fit_category = "Strong Fit"

        elif fit_score >= 50:

            fit_category = "Moderate Fit"

        else:

            fit_category = "Weak Fit"

        if fit_score >= 75:

            hiring_recommendation = (
                "Interview Recommended"
            )

        elif fit_score >= 50:

            hiring_recommendation = (
                "Needs Further Review"
            )

        else:

            hiring_recommendation = (
                "Not Recommended"
            )

        logger.info(
            "Phase 6 completed"
        )

        return {

            "semantic_score":

                semantic_result[
                    "semantic_score"
                ],

            "semantic_matches":
                semantic_result.get(
                   "matched",
                   []
                ),

               
            "semantic_missing":
               semantic_result.get(
                  "missing",
                   []
                ),

            "project_score":

                project_result[
                    "project_score"
                ],

            "relevant_projects":

                project_result[
                    "relevant_projects"
                ],

            "experience_relevance_score":

                experience_result[
                    "experience_relevance_score"
                ],

            "relevant_experience":

                experience_result[
                    "relevant_experience"
                ],

            "fit_score":

                fit_result[
                    "fit_score"
                ],

            "fit":

                fit_result[
                    "fit"
                ],

            "fit_category":

                fit_category,

            "hiring_recommendation":

                hiring_recommendation
        }