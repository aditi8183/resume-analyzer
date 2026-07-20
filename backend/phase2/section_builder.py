from phase2.heading_detector import (
    HeadingDetector
)

from phase2.section_classifier import (
    SectionClassifier
)


class SectionBuilder:

    @staticmethod
    def build(
        lines
    ):

        sections = {}

        current_section = (
            "summary"
        )

        sections[
            current_section
        ] = []

        for line in lines:

            line = line.strip()

            if not line:
                continue

            if (
                HeadingDetector
                .is_heading(
                    line
                )
            ):

                current_section = (

                    SectionClassifier
                    .classify(
                        line
                    )

                )

                if (
                    current_section
                    not in sections
                ):

                    sections[
                        current_section
                    ] = []

            else:

                sections[
                    current_section
                ].append(
                    line
                )

        return sections