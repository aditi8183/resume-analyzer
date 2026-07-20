class Validator:

    @staticmethod
    def validate_resume(data):

        required = [

            "skills",
            "education",
            "experience"

        ]

        for field in required:

            if field not in data:
                raise ValueError(
                    f"Missing field: {field}"
                )

        return True

    @staticmethod
    def validate_jd(data):

        required = [

            "required_skills",
            "required_experience"

        ]

        for field in required:

            if field not in data:
                raise ValueError(
                    f"Missing field: {field}"
                )

        return True