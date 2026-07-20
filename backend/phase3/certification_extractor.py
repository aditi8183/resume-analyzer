class CertificationExtractor:

    CERTIFICATION_KEYWORDS = [

        "aws",

        "azure",

        "google cloud",

        "gcp",

        "oracle",

        "ibm",

        "microsoft",

        "cisco",

        "nptel",

        "coursera",

        "udemy"
    ]

    def extract(

        self,

        sections

    ):

        certification_lines = sections.get(

            "certifications",

            []

        )

        certifications = []

        for line in certification_lines:

            text = line.lower()

            if any(

                keyword in text

                for keyword in

                self.CERTIFICATION_KEYWORDS

            ):

                certifications.append(

                    line.strip()

                )

        return certifications