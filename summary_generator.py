class SummaryGenerator:

    @staticmethod
    def generate(phase4_output):

        return {

            "top_skills":
                phase4_output.get(
                    "skills",
                    []
                )[:10],

            "experience_years":
                phase4_output.get(
                    "total_experience_years",
                    0
                ),

            "companies":
                phase4_output.get(
                    "companies",
                    []
                ),

            "degrees":
                phase4_output.get(
                    "degrees",
                    []
                )
        }