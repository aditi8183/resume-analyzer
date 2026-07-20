from logger import logger

from config.skill_weights import (
    SKILL_WEIGHTS
)


class SkillMatcher:

    ALIASES = {

        "ml":
            "machine learning",

        "dl":
            "deep learning",

        "nlp":
            "natural language processing",

        "cv":
            "computer vision",

        "js":
            "javascript"
    }

    CRITICAL_SKILLS = [

        "python",

        "sql",

        "machine learning"
    ]

    @staticmethod
    def normalize(
        skills
    ):

        normalized = []

        for skill in skills:

            skill = skill.lower().strip()

            skill = (

                SkillMatcher
                .ALIASES
                .get(
                    skill,
                    skill
                )
            )

            normalized.append(
                skill
            )

        return normalized

    @staticmethod
    def match(

        resume_skills,
        jd_skills

    ):

        resume_set = set(

            SkillMatcher
            .normalize(
                resume_skills
            )

        )

        jd_set = set(

            SkillMatcher
            .normalize(
                jd_skills
            )

        )

        matched = sorted(

            list(
                resume_set &
                jd_set
            )

        )

        missing = sorted(

            list(
                jd_set -
                resume_set
            )

        )

        total_weight = 0
        matched_weight = 0

        for skill in jd_set:

            weight = (

                SKILL_WEIGHTS
                .get(
                    skill,
                    1
                )

            )

            total_weight += weight

            if skill in matched:

                matched_weight += weight

        score = round(

            (
                matched_weight
                /
                max(
                    total_weight,
                    1
                )
            ) * 100,

            2

        )

        critical_missing = []

        for skill in (SkillMatcher.CRITICAL_SKILLS):

            if skill in jd_set and skill in missing:

                critical_missing.append(skill)

            

        logger.info(
            "Skill matching completed"
        )

        return {

            "matched":
                matched,

            "missing":
                missing,

            "critical_missing":
                critical_missing,

            "score":
                score

        }