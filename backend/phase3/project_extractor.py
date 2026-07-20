class ProjectExtractor:

    def extract(

        self,
        text

    ):

        projects = []

        lines = text.splitlines()

        project_keywords = [

            "project",
            "developed",
            "built",
            "implemented",
            "created",
            "designed",

            "cnn",
            "yolo",
            "computer vision",
            "deep learning",
            "machine learning",
            "nlp",
            "natural language processing",
            "detection",
            "recognition",
            "prediction"

        ]

        for line in lines:

            line = line.strip()

            if len(line) < 15:

                continue

            if any(

                keyword in line.lower()

                for keyword in project_keywords

            ):

                projects.append(
                    line
                )

        return list(
            set(projects)
        )