
class EducationExtractor:

    EDUCATION_KEYWORDS = [

        "b.tech",
        "btech",
        "bachelor of technology",

        "b.e",
        "be",
        "bachelor of engineering",

        "m.tech",
        "mtech",
        "master of technology",

        "m.e",
        "master of engineering",

        "bca",
        "bachelor of computer applications",

        "mca",
        "master of computer applications",

        "bsc",
        "b.sc",
        "bachelor of science",

        "msc",
        "m.sc",
        "master of science",

        "mba",
        "master of business administration",

        "phd",
        "doctorate",

        "diploma"
    ]

    def extract(

        self,

        sections

    ):
        print(
            "SECTION NAMES:", 
             sections.keys()
        )
        education = []

        for section_name, lines in sections.items():

            if any(

                word in section_name.lower()

                for word in [

                    "education",
                    "academic",
                    "qualification"
                ]

            ):  
                print(
                    "EDUCATION SECTION:",
                      lines
                )

                for line in lines:

                    text = line.lower()

                    if any(

                        keyword in text

                        for keyword in

                        self.EDUCATION_KEYWORDS

                    ):

                        education.append(

                            line.strip()

                        )

        return education

