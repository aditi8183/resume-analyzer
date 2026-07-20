from logger import logger


class ExplanationEngine:

    @staticmethod
    def generate(candidate):

        strengths = []
        weaknesses = []

        # -------------------------
        # Strengths
        # -------------------------

        if candidate.get(
            "education_score",
            0
        ) >= 80:

            strengths.append(
                "Strong educational background"
            )

        if candidate.get(
            "project_score",
            0
        ) >= 40:

            strengths.append(
                "Relevant project experience"
            )

        if candidate.get(
            "experience_relevance_score",
            0
        ) >= 40:

            strengths.append(
                "Good experience alignment"
            )

        matched_count = len(
            candidate.get(
                "matched_skills",
                []
            )
        )

        if matched_count >= 7:

            strengths.append(
                "Excellent alignment with core job requirements"
            )

        elif matched_count >= 5:

            strengths.append(
                "Strong skill coverage for the role"
            )

        elif matched_count >= 3:

            strengths.append(
                "Partially matches the required skill set"
            )

        if candidate.get(
            "semantic_score",
            0
        ) >= 40:

            strengths.append(
                "Good semantic alignment with job description"
            )

        # -------------------------
        # Weaknesses
        # -------------------------

        if candidate.get(
            "ats_score",
            0
        ) < 40:

            weaknesses.append(
                "Resume formatting may reduce ATS visibility"
            )

        # Critical missing skills

        for skill in candidate.get(
            "critical_missing",
            []
        ):

            weaknesses.append(
                f"Lacks required skill: {skill.upper() if skill.lower() == 'aws' else skill.title()}"
            )

        # Other missing skills

        non_critical_missing = [

            skill

            for skill in candidate.get(
                "missing_skills",
                []
            )

            if skill not in candidate.get(
                "critical_missing",
                []
            )

        ]

        if len(non_critical_missing) > 0:

            weaknesses.append(

                "Additional skill gaps in: "

                +

                ", ".join(

                    [
                        s.upper()
                        if s.lower() == "aws"
                        else s.title()

                        for s in non_critical_missing[:4]
                    ]

                )

            )

        if candidate.get(
            "project_score",
            0
        ) < 30:

            weaknesses.append(
                "Project portfolio shows limited relevance to target role"
            )

        if candidate.get(
            "education_score",
            0
        ) == 0:

            weaknesses.append(
                "Education details unclear or missing"
            )

        if candidate.get(
            "experience_relevance_score",
            0
        ) < 20:

            weaknesses.append(
                "Relevant industry experience appears limited"
            )

        if len(
            candidate.get(
                "critical_missing",
                []
            )
        ) >= 2:

            weaknesses.insert(

                0,

                "Multiple critical requirements are not satisfied"

            )

        logger.info(
            "Candidate explanation generated"
        )

        return {

            "strengths":
                strengths,

            "weaknesses":
                weaknesses

        }