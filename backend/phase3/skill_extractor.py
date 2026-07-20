import re

from phase3.skill_normalizer import (
    SkillNormalizer
)


class SkillExtractor:

    SKILLS = {

        "python",
        "java",
        "c",
        "c++",
        "sql",
        "mysql",
        "postgresql",
        "mongodb",

        "machine learning",
        "deep learning",
        "artificial intelligence",
        "computer vision",
        "natural language processing",

        "pandas",
        "numpy",
        "scikit-learn",
        "tensorflow",
        "keras",
        "pytorch",

        "spark",
        "pyspark",

        "docker",
        "kubernetes",

        "git",
        "github",

        "aws",
        "azure",
        "gcp",

        "opencv",
        "yolo",
        "kubeflow",

        "data science",
        "data analysis",
        "software engineering",
        "data scientist",
        "data analyst",

        "nlp",
        "cnn",

        "excel",
        "power bi",
        "tableau",

        "statistics",
        "data visualization",

        "hadoop",
        "hive",

        "flask",
        "django",
        "fastapi",

        "linux",
        "bash",

        "rest api",
        "api",

        "javascript",
        "html",
        "css",

        "react",
        "nodejs"
    }

    PARTIAL_PATTERNS = {

        "deep":
            "deep learning",

        "deep neural":
            "deep learning",

        "neural network":
            "deep learning",

        "neural networks":
            "deep learning",

        "nlp":
            "natural language processing",

        "natural language":
            "natural language processing",

        "computer vision":
            "computer vision",

        "vision":
            "computer vision",

        "statistics":
            "statistics",

        "statistical":
            "statistics",

        "data visualization":
            "data visualization",

        "visualization":
            "data visualization"
    }

    def extract(

        self,

        text

    ):

        text = text.lower()

        found = set()

        for skill in self.SKILLS:

            pattern = (

                r"\b"

                +

                re.escape(skill)

                +

                r"\b"
            )

            if re.search(

                pattern,

                text
            ):

                found.add(

                    SkillNormalizer.normalize(
                        skill
                    )
                )

        for phrase, skill in (

            self.PARTIAL_PATTERNS.items()
        ):

            if phrase in text:

                found.add(

                    SkillNormalizer.normalize(
                        skill
                    )
                )

        return sorted(
            list(found)
        )
    