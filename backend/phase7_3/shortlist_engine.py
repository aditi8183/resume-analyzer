from logger import logger


class ShortlistEngine:

    @staticmethod
    def shortlist(
        candidates,
        threshold=75
    ):

        shortlisted = []

        rejected = []

        for candidate in candidates:

            score = candidate.get(
                "ats_score",
                0
            )

            if score >= threshold:

                candidate[
                    "status"
                ] = "Shortlisted"

                shortlisted.append(
                    candidate
                )

            else:

                candidate[
                    "status"
                ] = "Rejected"

                rejected.append(
                    candidate
                )

        logger.info(
            "Shortlisting completed"
        )

        return {

            "shortlisted":
                shortlisted,

            "rejected":
                rejected,

            "total":
                len(candidates)
        }