import csv
import os

from logger import logger


class CSVExporter:

    @staticmethod
    def export(
        data,
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
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(
                file
            )

            writer.writerow(
                [
                    "Metric",
                    "Value"
                ]
            )

            for key, value in data.items():

                writer.writerow(
                    [
                        key,
                        str(value)
                    ]
                )

        logger.info(
            f"CSV exported: {output_path}"
        )