from phase4.skill_matcher import SkillMatcher

result = SkillMatcher.match(

    ["python", "sql"],

    ["python", "sql", "aws"]
)

print(result)