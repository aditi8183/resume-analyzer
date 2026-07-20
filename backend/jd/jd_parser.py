# jd/jd_parser.py

from jd.jd_extractor import (
    JDExtractor
)

from phase3.skill_extractor import (
    SkillExtractor
)

from phase3.keyword_extractor import (
    KeywordExtractor
)

from phase3.experience_extractor import (
    ExperienceExtractor
)

from logger import logger


class JDParser:

    def parse(
        self,
        file_path
    ):

        text = (
            JDExtractor()
            .extract(
                file_path
            )
        )

        skills = (
            SkillExtractor()
            .extract(
                text
            )
        )

        keywords = (
            KeywordExtractor()
            .extract(
                text
            )
        )

        experience = (
            ExperienceExtractor()
            .extract(
                text
            )
        )

        logger.info(
            "JD parsing completed"
        )

        return {

            "skills":
                skills,

            "keywords":
                keywords,

            "experience":
                experience,

            "text":
                text,
            "required_skills": 
               skills,

            "critical_skills": 
               skills[:5]

        }