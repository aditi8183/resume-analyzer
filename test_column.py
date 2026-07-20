from phase1.resume_extractor import (
    ResumeExtractor
)

from phase2.column_detector import (
    ColumnDetector
)

extractor = ResumeExtractor()

phase1_output = extractor.extract(
    "cv (1).pdf"
)

detector = ColumnDetector()

columns = detector.detect(
    phase1_output["blocks"]
)

print(
    "\nDetected Columns:",
    columns
)