from phase3.skill_extractor import (
    SkillExtractor
)
from phase3.name_extractor import NameExtractor
from phase3.keyword_extractor import (
    KeywordExtractor
)

from phase3.experience_extractor import (
    ExperienceExtractor
)

from phase3.project_extractor import (
    ProjectExtractor
)

from phase3.experience_detail_extractor import (
    ExperienceDetailExtractor
)

from phase3.education_extractor import (
    EducationExtractor
)

from phase3.certification_extractor import (
    CertificationExtractor
)

from config.skill_ontology import (
    SKILL_ONTOLOGY
)

from logger import logger


class Phase3Parser:

    @staticmethod
    def expand_skills(skills):

        expanded_skills = set(

            skill.lower()
            for skill in skills

        )

        for parent_skill, child_skills in (

            SKILL_ONTOLOGY.items()

        ):

            for child in child_skills:

                if child.lower() in expanded_skills:

                    expanded_skills.add(

                        parent_skill.lower()

                    )

                    break

        return list(

            expanded_skills

        )

    def parse(

        self,
        phase2_output

    ):

        text = ""

        for section in (

            phase2_output[
                "sections"
            ]
            .values()

        ):

            text += "\n".join(
                section
            )

        name = NameExtractor.extract(text)

        skills = (

            SkillExtractor()
            .extract(
                text
            )

        )

        skills = (

            self.expand_skills(
                skills
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
                phase2_output["sections"]
            )

        )

        projects = (

            ProjectExtractor()
            .extract(
                text
            )

        )

        experience_details = (

            ExperienceDetailExtractor()
            .extract(
                text
            )

        )

        education = (

            EducationExtractor()
            .extract(

                phase2_output[
                    "sections"
                ]

            )

        )
        print(
            "PHASE3 EDUCATION:",
             education
        )

        certifications = (

            CertificationExtractor()
            .extract(

                phase2_output[
                    "sections"
                ]

            )

        )
        print("Phase2.keys:")
        print(phase2_output.keys())

        logger.info(
            "Phase 3 completed"
        )
        print("CANDIDATE NAME:", name)

        return {

            "name":
                name,

            "skills":
                skills,

            "keywords":
                keywords,

            "experience":
                experience,

            "projects":
                projects,

            "experience_details":
                experience_details,

            "education":
                education,

            "certifications":
                certifications
        }
 







