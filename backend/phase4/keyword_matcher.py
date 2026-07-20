from logger import logger


class KeywordMatcher:

    @staticmethod
    def match(
        resume_keywords,
        jd_keywords
    ):

        resume_set = set(
            resume_keywords
        )

        jd_set = set(
            jd_keywords
        )

        matched = sorted(
            list(
                resume_set &
                jd_set
            )
        )
        missing = sorted(
            list(
               jd_set - resume_set
            )
        )

        score = 0

        if len(jd_set) > 0:

            score = round(

                (
                    len(matched)
                    /
                    len(jd_set)
                )
                * 100,

                2
            )
        score = 0

        TECH_KEYWORDS = {
            "python",
            "sql",
            "machine learning",
            "deep learning",
            "tensorflow",
            "pytorch",
            "react",
            "javascript",
            "aws",
           "docker",
          "kubernetes"
        }

        total_weight = 0
        matched_weight = 0

        for keyword in jd_set:

          weight = 3 if keyword.lower() in TECH_KEYWORDS else 1

          total_weight += weight

          if keyword in matched:

              matched_weight += weight

        if total_weight > 0:

           score = round(

              (matched_weight / total_weight) * 100,

               2

            )

        logger.info(
            "Keyword matching completed"
        )

        return {

            "matched":
                matched,
            "missing":
              missing,

            "score":
                score
        }