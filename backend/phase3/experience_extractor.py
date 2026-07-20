import re
from datetime import datetime


class ExperienceExtractor:

    def extract(

        self,

        data

    ):

        # =====================
        # Resume Sections Input
        # =====================

        if isinstance(

            data,

            dict

        ):

            experience_text = ""

            for section_name, content in (

                data.items()

            ):

                if (

                    "work" in section_name.lower()

                    or

                    "experience" in section_name.lower()

                ):

                    experience_text += "\n".join(
                        content
                    )

        # =====================
        # JD Text Input
        # =====================

        elif isinstance(

            data,

            str

        ):

            experience_text = data

        else:

            return 0

        if not experience_text:

            return 0

        # =====================
        # Explicit Years
        # Example:
        # 5 years
        # 3+ years
        # 2.5 years
        # =====================

        matches = re.findall(

            r"(\d+(?:\.\d+)?)\+?\s*years",

            experience_text.lower()

        )

        if matches:

            return max(

                float(x)

                for x in matches

            )

        # =====================
        # Date Range Detection
        # Example:
        # Jan 2019 to Till Date
        # Jan 2019 - Present
        # =====================

        month_map = {

            "jan": 1,
            "feb": 2,
            "mar": 3,
            "apr": 4,
            "may": 5,
            "jun": 6,
            "jul": 7,
            "aug": 8,
            "sep": 9,
            "oct": 10,
            "nov": 11,
            "dec": 12
        }

        date_pattern = re.findall(

            r"(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\s+(\d{4})\s+(?:to|-)\s+(?:till date|present|current)",

            experience_text.lower()

        )

        if date_pattern:

            month_str, year_str = (

                date_pattern[0]

            )

            start_date = datetime(

                int(year_str),

                month_map[
                    month_str
                ],

                1

            )

            today = datetime.now()

            months = (

                (today.year - start_date.year)

                * 12

                +

                (
                    today.month
                    - start_date.month
                )

            )

            return round(

                months / 12,

                1

            )

        return 0