from logger import logger


class GapAnalyzer:

    CRITICAL_SKILLS = [

        "python",
        "machine learning",
        "sql",
        "aws"
    ]

    @staticmethod
    def analyze(

        resume_exp,
        jd_exp,
        missing_skills

    ):

        gap = max(

            jd_exp -
            resume_exp,

            0
        )

        critical_missing = [

            skill

            for skill
            in missing_skills

            if skill in
            GapAnalyzer.CRITICAL_SKILLS
        ]

        logger.info(
            "Gap analysis completed"
        )

        return {

            "candidate":
                resume_exp,

            "required":
                jd_exp,

            "gap":
                gap,

            "critical_missing":
                critical_missing
        }