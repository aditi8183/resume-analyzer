'''from phase6.semantic_matcher import (
    SemanticMatcher
)

print(

    SemanticMatcher
    .similarity(

        "machine learning",

        "ml"

    )

)

print(

    SemanticMatcher
    .similarity(

        "python",

        "java"

    )

)'''
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


phase1_output = (

    ResumeExtractor()
    .extract(
        "cv (1).pdf"
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
        "sample_jd.txt"
    )

)

phase4_result = (

    Matcher()
    .match(

        resume_profile,

        jd_profile

    )

)

phase6_result = (

    SemanticEngine()
    .analyze(

        resume_profile,

        jd_profile,

        phase4_result

    )

)

print(
    "\nPHASE 6 RESULT\n"
)

print(
    phase6_result
)