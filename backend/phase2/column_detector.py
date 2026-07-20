class ColumnDetector:

    def detect(
        self,
        blocks
    ):

        if not blocks:

            return {

                "columns": 1,

                "split_x": None

            }

        x_positions = []

        for block in blocks:

            if "x0" in block:

                x_positions.append(
                    block["x0"]
                )

        if len(x_positions) < 5:

            return {

                "columns": 1,

                "split_x": None

            }

        x_positions.sort()

        max_gap = 0

        split_x = None

        for i in range(
            len(x_positions) - 1
        ):

            gap = (

                x_positions[i + 1]
                -
                x_positions[i]

            )

            if gap > max_gap:

                max_gap = gap

                split_x = (

                    x_positions[i]
                    +
                    x_positions[i + 1]

                ) / 2

        page_width = max(
            x_positions
        )

        threshold = (
            page_width * 0.20
        )

        if max_gap > threshold:

            return {

                "columns": 2,

                "split_x": split_x

            }

        return {

            "columns": 1,

            "split_x": None

        }