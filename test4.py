from phase1.resume_extractor import ResumeExtractor
from phase2.layout_parser import LayoutParser
from phase3.phase_parser import Phase3Parser

from jd.jd_parser import JDParser

from phase4.matcher import Matcher


phase1_output = (
    ResumeExtractor()
    .extract("cv (1).pdf")
)

phase2_output = (
    LayoutParser()
    .parse(phase1_output)
)

resume_profile = (
    Phase3Parser()
    .parse(phase2_output)
)

jd_profile = (
    JDParser()
    .parse("sample_jd.txt")
)

result = (
    Matcher()
    .match(
        resume_profile,
        jd_profile
    )
)

print(result)