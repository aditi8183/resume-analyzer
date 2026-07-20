from phase1.resume_extractor import ResumeExtractor
from phase2.layout_parser import LayoutParser
from phase3.phase_parser import Phase3Parser

resume = (
    ResumeExtractor()
    .extract("cv (1).pdf")
)

phase2 = (
    LayoutParser()
    .parse(resume)
)

phase3 = (
    Phase3Parser()
    .parse(phase2)
)

print(phase3)