class ExperienceDetailExtractor:

    def extract(

        self,
        text

    ):

        experiences = []

        lines = text.splitlines()

        experience_keywords = [

            "intern",
            "developer",
            "engineer",
            "analyst",
            "consultant",
            "manager",
            "associate",
            "worked",
            "working",
            "employment"

        ]

        for line in lines:

            line = line.strip()

            if len(line) < 10:

                continue

            if "m.tech" in line.lower():

                continue

            if "b.tech" in line.lower():

                continue

            if "university" in line.lower():

                continue

            if any(

                keyword in line.lower()

                for keyword in experience_keywords

            ):

                experiences.append(
                    line
                )

        return list(
            set(experiences)
        )