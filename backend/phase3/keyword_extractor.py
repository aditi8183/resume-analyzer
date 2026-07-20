# phase3/keyword_extractor.py

import re


class KeywordExtractor:

    def extract(
        self,
        text
    ):

        words = re.findall(
            r"\b[a-zA-Z]{3,}\b",
            text.lower()
        )

        stopwords = {

            "the",
            "and",
            "for",
            "with",
            "from",
            "that",
            "this",
            "have",
            "has",
            "are",
            "was",
            "were"
        }

        keywords = []

        for word in words:

            if word not in stopwords:

                keywords.append(
                    word
                )

        return list(
            set(keywords)
        )