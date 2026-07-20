from logger import logger

from phase2.reading_order import (
    ReadingOrder
)

from phase2.column_detector import (
    ColumnDetector
)

from phase2.section_builder import (
    SectionBuilder
)


class LayoutParser:

    def parse(
        self,
        phase1_output
    ):

        blocks = phase1_output[
            "blocks"
        ]

        layout_info = (

            ColumnDetector()
            .detect(
                blocks
            )

        )

        lines = (

            ReadingOrder
            .sort_blocks(

                blocks,

                layout_info

            )

        )

        sections = (

            SectionBuilder
            .build(
                lines
            )

        )

        logger.info(
            "Layout parsing completed"
        )

        return {

            "sections":
                sections,

            "layout":
                layout_info
        }