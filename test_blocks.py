from phase1.resume_extractor import (
    ResumeExtractor
)

data = (
    ResumeExtractor()
    .extract("cv (1).pdf")
)

print(
    data["blocks"][:5]
)