class SectionClassifier:

    @staticmethod
    def classify(
        heading
    ):

        heading = (
            heading.lower()
            .strip()
        )

        mapping = {

            "education":
                "education",

            "experience":
                "experience",

            "work experience":
                "experience",

            "skills":
                "skills",

            "projects":
                "projects",

            "certifications":
                "certifications",

            "summary":
                "summary",

            "profile":
                "summary",

            "objective":
                "summary",
            
            "about":
                "summary",

            "activities":
                "activities"
        }

        return mapping.get(
            heading,
            "other"
        )