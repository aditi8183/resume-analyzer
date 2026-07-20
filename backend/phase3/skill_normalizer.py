# phase3/skill_normalizer.py

class SkillNormalizer:

    SKILL_MAP = {

        # Machine Learning
        "ml": "machine learning",
        "machine-learning": "machine learning",

        # NLP
        "nlp": "natural language processing",

        # Computer Vision
        "cv": "computer vision",

        # AI
        "ai": "artificial intelligence",

        # Languages
        "js": "javascript",
        "py": "python",
        "c plus plus": "c++",

        # SQL Variants
        "mysql": "sql",
        "postgresql": "sql",
        "postgres": "sql",
        "sqlite": "sql",
        "mssql": "sql",

        # Deep Learning
        "tensorflow": "deep learning",
        "pytorch": "deep learning",
        "keras": "deep learning",

        # Scikit Learn Variants
        "sklearn": "scikit-learn",
        "scikit learn": "scikit-learn",

        # Data Science
        "data science": "data scientist",

        # Cloud
        "amazon web services": "aws"
    }

    @classmethod
    def normalize(
        cls,
        skill
    ):

        skill = (
            skill
            .strip()
            .lower()
        )

        return cls.SKILL_MAP.get(
            skill,
            skill
        )