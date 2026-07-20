import json
import os

from logger import logger


class RankingExporter:

    @staticmethod
    def export(

        rankings,

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

                rankings,

                file,

                indent=4

            )

        logger.info(

            f"Ranking exported: "

            f"{output_path}"

        )