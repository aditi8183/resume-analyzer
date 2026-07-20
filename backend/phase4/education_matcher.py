
from config.education_weights import (
    EDUCATION_WEIGHTS
)


DEGREE_ALIASES = {

    "phd": [
        "phd",
        "doctorate",
        "doctoral"
    ],

    "m.tech": [
        "m.tech",
        "mtech",
        "master of technology"
    ],

    "m.e": [
        "m.e",
        "me",
        "master of engineering"
    ],

    "mba": [
        "mba",
        "master of business administration"
    ],

    "mca": [
        "mca",
        "master of computer applications"
    ],

    "msc": [
        "msc",
        "m.sc",
        "master of science"
    ],

    "b.tech": [
        "b.tech",
        "btech",
        "bachelor of technology"
    ],

    "b.e": [
        "b.e",
        "be",
        "bachelor of engineering"
    ],

    "bca": [
        "bca",
        "bachelor of computer applications"
    ],

    "bsc": [
        "bsc",
        "b.sc",
        "bachelor of science"
    ],

    "diploma": [
        "diploma"
    ]
}


class EducationMatcher:

    @staticmethod
    def match(

        education_list

    ):
        print(
            "EDUCATION LIST:", 
             education_list
        )
        print(
            "MATCHER RECEIVED:",
             education_list
        )

        best_score = 0

        matched_degree = None

        for education in education_list:

            text = education.lower()

            for degree, aliases in (

                DEGREE_ALIASES.items()

            ):

                for alias in aliases:

                    if alias in text:

                        score = EDUCATION_WEIGHTS.get(
                            degree,
                            0
                        )

                        if score > best_score:

                            best_score = score

                            matched_degree = degree

        return {

            "education_score":
                best_score,

            "matched_degree":
                matched_degree

        }
