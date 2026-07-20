import re


class HeadingDetector:

    HEADINGS = {

        "education",
        "experience",
        "work experience",
        "projects",
        "skills",
        "certifications",
        "summary",
        "profile",
        "objective",
        "activities",
        "about"

    }

    @classmethod
    def is_heading(

        cls,
        line

    ):

        cleaned = (

            re.sub(

                r"[^a-zA-Z ]",

                "",

                line

            )

            .lower()

            .strip()

        )

        return (

            cleaned
            in
            cls.HEADINGS

        )