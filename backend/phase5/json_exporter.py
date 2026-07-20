import json
import os

from logger import logger


class JSONExporter:

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
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

        logger.info(
            f"JSON exported: {output_path}"
        )