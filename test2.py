'''from phase1.resume_extractor import ResumeExtractor
from phase2.layout_parser import LayoutParser

extractor = ResumeExtractor()
phase1_output = extractor.extract("cv (1).pdf")

parser = LayoutParser()
phase2_output = parser.parse(phase1_output)

print(phase2_output)
from phase1.resume_extractor import ResumeExtractor
from phase2.layout_parser import LayoutParser

phase1_output = (
    ResumeExtractor()
    .extract("cv (1).pdf")
)

phase2_output = (
    LayoutParser()
    .parse(phase1_output)
)

print("\nSECTION NAMES\n")

for key in phase2_output["sections"]:

    print(key)'''
print("\nFULL SECTIONS\n")

from phase1.resume_extractor import (
    ResumeExtractor
)

from phase2.layout_parser import (
    LayoutParser
)

extractor = ResumeExtractor()

phase1_output = (

    extractor.extract(
        "cv (1).pdf"
    )

)

parser = LayoutParser()

phase2_output = (

    parser.parse(
        phase1_output
    )

)

print("\nSECTION CONTENTS\n")

for section_name, content in (

    phase2_output[
        "sections"
    ].items()

):

    print("\n===================")
    print(section_name.upper())
    print("===================")

    print(content)