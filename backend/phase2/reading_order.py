class ReadingOrder:

    @staticmethod
    def sort_blocks(

        blocks,

        layout_info

    ):

        columns = layout_info[
            "columns"
        ]

        if columns == 1:

            sorted_blocks = sorted(

                blocks,

                key=lambda b: (

                    b["page"],
                    b["y0"],
                    b["x0"]

                )

            )

        else:

            split_x = layout_info[
                "split_x"
            ]

            left_blocks = []

            right_blocks = []

            for block in blocks:

                if (

                    block["x0"]

                    <

                    split_x

                ):

                    left_blocks.append(
                        block
                    )

                else:

                    right_blocks.append(
                        block
                    )

            left_blocks.sort(

                key=lambda b: (

                    b["page"],
                    b["y0"]

                )

            )

            right_blocks.sort(

                key=lambda b: (

                    b["page"],
                    b["y0"]

                )

            )

            sorted_blocks = (

                left_blocks

                +

                right_blocks

            )

        lines = []

        for block in sorted_blocks:

            text = block.get(
                "text",
                ""
            )

            for line in text.split(
                "\n"
            ):

                line = line.strip()

                if line:

                    lines.append(
                        line
                    )

        return lines