import os

from logger import logger


class ReportGenerator:

    @staticmethod
    def generate(
        result,
        output_path
    ):

        os.makedirs(
            os.path.dirname(
                output_path
            ),
            exist_ok=True
        )

        with open(
            output_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                "===== ATS REPORT =====\n\n"
            )

            file.write(

                f"ATS Score: "
                f"{result['scores']['ats_score']}\n"

            )

            file.write(

                f"Skill Score: "
                f"{result['scores']['skill_score']}\n"

            )

            file.write(

                f"Keyword Score: "
                f"{result['scores']['keyword_score']}\n"

            )

            file.write(

                f"Experience Score: "
                f"{result['scores']['experience_score']}\n"

            )

            file.write(

                f"\nJob Level: "
                f"{result['job_level']}\n\n"

            )

            file.write(
                "Matched Skills:\n"
            )

            for skill in result[
                "matching"
            ][
                "matched_skills"
            ]:

                file.write(
                    f"- {skill}\n"
                )

            file.write(
                "\nMissing Skills:\n"
            )

            for skill in result[
                "gaps"
            ][
                "missing_skills"
            ]:

                file.write(
                    f"- {skill}\n"
                )

            file.write(
                "\nCritical Missing Skills:\n"
            )

            for skill in result[
                "gaps"
            ][
                "critical_missing"
            ]:

                file.write(
                    f"- {skill}\n"
                )

            file.write(
                "\nRecommendations:\n"
            )

            for recommendation in result[
                "recommendations"
            ]:

                file.write(
                    f"- {recommendation}\n"
                )

        logger.info(
            f"Report generated: {output_path}"
        )