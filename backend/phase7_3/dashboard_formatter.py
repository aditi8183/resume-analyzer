from logger import logger


class DashboardFormatter:

    @staticmethod
    def candidate_view(
        result
    ):

        return {

            "ats_score":

                result[
                    "scores"
                ][
                    "ats_score"
                ],

            "matched_skills":

                result[
                    "matching"
                ][
                    "matched_skills"
                ],

            "missing_skills":

                result[
                    "gaps"
                ][
                    "missing_skills"
                ],

            "recommendations":

                result[
                    "recommendations"
                ]
        }

    @staticmethod
    def recruiter_view(
        candidate
    ):

        return {

            "candidate_name":

                candidate[
                    "name"
                ],

            "ats_score":

                candidate[
                    "ats_score"
                ],

            "status":

                candidate.get(
                    "status",
                    "Pending"
                )
        }