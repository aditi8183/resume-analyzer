from sentence_transformers import (
    SentenceTransformer
)

from sentence_transformers.util import (
    cos_sim
)

from logger import logger


class SemanticMatcher:

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    @staticmethod
    def similarity(

        text1,
        text2

    ):

        emb1 = (

            SemanticMatcher
            .model
            .encode(
                text1,
                convert_to_tensor=True
            )
        )

        emb2 = (

            SemanticMatcher
            .model
            .encode(
                text2,
                convert_to_tensor=True
            )
        )

        score = (

            cos_sim(
                emb1,
                emb2
            )
            .item()
        )

        logger.info(
            "Semantic similarity calculated"
        )

        return round(
            score,
            4
        )