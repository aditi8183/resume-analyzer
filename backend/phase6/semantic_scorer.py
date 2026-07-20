from logger import logger

from phase6.semantic_matcher import (
    SemanticMatcher
)


class SemanticScorer:

    THRESHOLD = 0.70

    @staticmethod
    def score(

        resume_skills,
        jd_skills,
        projects=None,
        experiences=None,
        jd_text=""

    ):

        matched = []

        missing = []

        scores = []

        # -------------------------
        # Skill Semantic Matching
        # -------------------------

        for jd_skill in jd_skills:

            best_score = 0

            for resume_skill in resume_skills:

                similarity = (

                    SemanticMatcher
                    .similarity(

                        resume_skill,

                        jd_skill

                    )

                )

                if similarity > best_score:

                    best_score = similarity

            scores.append(
                best_score
            )

            if best_score >= (

                SemanticScorer
                .THRESHOLD

            ):

                matched.append(
                    jd_skill
                )

            else:

                missing.append(
                    jd_skill
                )

        # -------------------------
        # Project Semantic Score
        # -------------------------

        project_score = 0

        if projects:

            project_scores = []

            for project in projects:

                score = (

                    SemanticMatcher
                    .similarity(

                        project,

                        jd_text

                    )

                )

                project_scores.append(
                    score
                )

            project_score = (

                sum(
                    project_scores
                )

                /

                max(
                    len(
                        project_scores
                    ),
                    1
                )

            )

        # -------------------------
        # Experience Semantic Score
        # -------------------------

        experience_score = 0

        if experiences:

            experience_scores = []

            for experience in experiences:

                score = (

                    SemanticMatcher
                    .similarity(

                        experience,

                        jd_text

                    )

                )

                experience_scores.append(
                    score
                )

            experience_score = (

                sum(
                    experience_scores
                )

                /

                max(
                    len(
                        experience_scores
                    ),
                    1
                )

            )

        # -------------------------
        # Combined Semantic Score
        # -------------------------

        skill_component = (

            sum(scores)

            /

            max(
                len(scores),
                1
            )

        )

        semantic_score = round(

            (

                skill_component * 0.50

            )

            +

            (

                project_score * 0.25

            )

            +

            (

                experience_score * 0.25

            )

            ,

            4

        )

        semantic_score = round(

            semantic_score * 100,

            2

        )

        logger.info(
            "Semantic scoring completed"
        )

        return {

            "matched":
                matched,

            "missing":
                missing,

            "semantic_score":
                semantic_score,

            "project_component":
                round(
                    project_score * 100,
                    2
                ),

            "experience_component":
                round(
                    experience_score * 100,
                    2
                )

        }