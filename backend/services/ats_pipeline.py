from phase1.resume_extractor import (
    ResumeExtractor
)

from phase2.layout_parser import (
    LayoutParser
)

from phase3.phase_parser import (
    Phase3Parser
)

from jd.jd_parser import (
    JDParser
)

from phase4.matcher import (
    Matcher
)

from phase6.semantic_engine import (
    SemanticEngine
)

from phase7.explainability_engine import (
    ExplainabilityEngine
)


class ATSPipeline:

    @staticmethod
    def run(

        resume_file,

        jd_file

    ):

        phase1_output = (

            ResumeExtractor()
            .extract(
                resume_file
            )

        )

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

        jd_profile = (

            JDParser()
            .parse(
                jd_file
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

        explanation = (

            ExplainabilityEngine()
            .generate(

                phase4_result,

                semantic_result

            )

        )

        print("RESUME PROFILE:")
        print(resume_profile)

        return {

            "resume_profile":
                resume_profile,

            "jd_profile":
                jd_profile,

            "result":
                phase4_result,

            "semantic":
                semantic_result,

            "explanation":
                explanation
        }