
from phase1.resume_extractor import ResumeExtractor

extractor = ResumeExtractor()

result = extractor.extract("cv (1).pdf")

print(type(result))
print(result.keys())