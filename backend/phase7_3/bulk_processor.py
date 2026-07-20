import os
from logger import logger
import traceback
from phase1.resume_extractor import (
    ResumeExtractor
)

from phase2.layout_parser import (
    LayoutParser
)

from phase3.phase_parser import (
    Phase3Parser
)

from phase4.matcher import (
    Matcher
)

from phase6.semantic_engine import (
    SemanticEngine
)


class BulkProcessor:

    @staticmethod
    def process(

        resume_files,

        jd_profile

    ):

        results = []

        for resume_file in (

            resume_files

        ):

            try:

                phase1_output = (

                    ResumeExtractor()
                    .extract(
                        resume_file
                    )

                )
                print("\nPHASE 1 OUTPUT:")
                print(phase1_output)

                phase2_output = (

                    LayoutParser()
                    .parse(
                        phase1_output
                    )

                )

                resume_profile = (

                    Phase3Parser()
                    .parse(
                        phase2_output
                    )

                )

                phase4_result = (

                    Matcher()
                    .match(

                        resume_profile,

                        jd_profile

                    )

                )

                semantic_result = (

                    SemanticEngine()
                    .analyze(

                        resume_profile,

                        jd_profile,

                        phase4_result

                    )

                )

                matched_skills = phase4_result["matching"].get(
                    "matched_skills",
                    []
                )

                missing_skills = phase4_result["gaps"].get(
                    "missing_skills",
                    []
                )

                total_skills = (

                    len(matched_skills)

                    +

                    len(missing_skills)

                )

                skill_match_percentage = (

                    round(

                        (len(matched_skills) / total_skills) * 100,

                        2

                    )

                    if total_skills > 0

                    else 0

                )

                results.append(

                    {

                        "resume":

                            resume_file,
                        "resume_url":
                           f"http://127.0.0.1:8000/resumes/{os.path.basename(resume_file)}",

                        "result":

                            {

                                "resume_profile":
                                    resume_profile,

                                "jd_profile":
                                    jd_profile,

                                "result":
                                    phase4_result,

                                "semantic":
                                    semantic_result,

                                "skill_match_percentage":
                                    skill_match_percentage,

                                "matched_skill_count":
                                    len(
                                        matched_skills
                                    ),

                                "missing_skill_count":
                                    len(
                                        missing_skills
                                    )

                            }

                    }

                )

            except Exception as e:
                print("\n\nFULL TRACEBACK:\n")
                traceback.print_exc()


                logger.error(

                    f"Failed: "

                    f"{resume_file}"

                    f" | {e}"

                )

        logger.info(
            "Bulk processing completed"
        )

        return results