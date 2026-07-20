from logger import logger

from phase6.semantic_matcher import (
    SemanticMatcher
)


class ProjectMatcher:

    THRESHOLD = 0.60

    COMPLEXITY_KEYWORDS = [

        "machine learning",
        "deep learning",
        "computer vision",
        "natural language processing",
        "nlp",
        "cnn",
        "transformer",
        "bert",
        "gpt",
        "yolo",
        "object detection",
        "recommendation system",
        "predictive model",
        "forecasting",
        "data pipeline",
        "spark",
        "pyspark",
        "kubeflow",
        "aws",
        "docker",
        "kubernetes"
    ]

    @staticmethod
    def match(

        projects,
        jd_skills

    ):

        relevant_projects = []

        project_scores = []

        complexity_score = 0

        for project in projects:

            best_score = 0

            for skill in jd_skills:

                score = (

                    SemanticMatcher
                    .similarity(

                        project,
                        skill

                    )

                )

                if score > best_score:

                    best_score = score

            project_scores.append(
                best_score
            )

            if best_score >= (

                ProjectMatcher
                .THRESHOLD

            ):

                relevant_projects.append(
                    project
                )

            lower_project = project.lower()

            for keyword in (

                ProjectMatcher
                .COMPLEXITY_KEYWORDS

            ):

                if keyword in lower_project:

                    complexity_score += 5

        relevance_score = 0

        if len(project_scores) > 0:

            relevance_score = (

                sum(project_scores)

                /

                len(project_scores)

            ) * 100

        project_score = round(

            min(

                (

                    relevance_score * 0.7

                )

                +

                (

                    complexity_score * 0.3

                ),

                100

            ),

            2

        )

        logger.info(
            "Project matching completed"
        )

        return {

            "relevant_projects":
                relevant_projects,

            "scores":
                project_scores,

            "project_score":
                project_score
        }