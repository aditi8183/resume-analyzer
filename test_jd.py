from jd.jd_parser import JDParser

parser = JDParser()

result = parser.parse(
    "sample_jd.txt"
)

print(result)