from logger import logger


class RecruiterSummary:

    @staticmethod
    def generate(
        candidates
    ):

        total = len(
            candidates
        )

        shortlisted = len(

            [

                c

                for c in candidates

                if c.get(
                    "status"
                )
                ==
                "Shortlisted"

            ]

        )

        rejected = len(

            [

                c

                for c in candidates

                if c.get(
                    "status"
                )
                ==
                "Rejected"

            ]

        )

        average_score = 0

        if total > 0:

            average_score = round(

                sum(

                    c.get(
                        "ats_score",
                        0
                    )

                    for c in candidates

                )

                /

                total,

                2

            )

        top_score = 0

        if total > 0:

            top_score = max(

                c.get(
                    "ats_score",
                    0
                )

                for c in candidates

            )

        logger.info(
            "Recruiter summary generated"
        )

        return {

            "total_candidates":
                total,

            "shortlisted":
                shortlisted,

            "rejected":
                rejected,

            "average_score":
                average_score,

            "top_score":
                top_score
        }