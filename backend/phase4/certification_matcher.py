from config.certification_weights import (
    CERTIFICATION_WEIGHTS
)


class CertificationMatcher:

    @staticmethod
    def match(

        certifications

    ):

        score = 0

        matched = []

        for cert in certifications:

            text = cert.lower()

            for keyword, value in (

                CERTIFICATION_WEIGHTS.items()

            ):

                if keyword in text:

                    score += value

                    matched.append(

                        keyword

                    )

        score = min(

            score,

            100

        )

        return {

            "certification_score":
                score,

            "matched_certifications":
                matched
        }