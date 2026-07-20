from logger import logger

from phase7_1.project_matcher import (
    ProjectMatcher
)

from phase7_1.project_scorer import (
    ProjectScorer
)


class ProjectEngine:

    def analyze(

        self,

        resume_profile,
        jd_profile

    ):

        projects = (

            resume_profile
            .get(

                "projects",

                []

            )

        )

        result = (

            ProjectMatcher
            .match(

                projects,

                jd_profile[
                    "skills"
                ]

            )

        )

        project_score = (

            ProjectScorer
            .score(

                result[
                    "scores"
                ]

            )

        )

        logger.info(
            "Project relevance analysis completed"
        )

        return {

            "project_score":
                project_score,

            "relevant_projects":

                result[
                    "relevant_projects"
                ]
        }