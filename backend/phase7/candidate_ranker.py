from logger import logger

from phase7.ranking_engine import (
    RankingEngine
)

from phase7.explanation_engine import (
    ExplanationEngine
)


class CandidateRanker:

    @staticmethod
    def rank(

        candidates

    ):

        ranked = []

        for candidate in candidates:

            score =(

                RankingEngine
                .calculate(

                    candidate[
                        "ats_score"
                    ],

                    candidate[
                        "semantic_score"
                    ],

                    candidate[
                        "fit_score"
                    ],

                    candidate.get(
                        "project_score",
                        0
                    ),

                    candidate.get(
                        "experience_relevance_score",
                        0
                    ),

                    candidate.get(
                        "education_score",
                        0
                    ),

                    candidate.get(
                        "certification_score",
                        0
                    ),

                    len(
                        candidate.get(
                          "critical_missing",
                           []
                        )

                    )  ,
                    len(
                        candidate.get(
                           "matched_skills",
                            []
                        )
                    ),

                    len(
                       candidate.get(
                            "missing_skills",
                            []
                        )
                    ) 
                )

            )

            candidate[
                "final_score"
            ] = score

            explanation = (

                ExplanationEngine
                .generate(

                    candidate

                )

            )

            candidate[
                "strengths"
            ] = explanation[
                "strengths"
            ]

            candidate[
                "weaknesses"
            ] = explanation[
                "weaknesses"
            ]

            ranked.append(
                candidate
            )

        ranked.sort(

            key=lambda x:
                x[
                    "final_score"
                ],

            reverse=True

        )

        rank = 1

        for candidate in ranked:

            candidate[
                "rank"
            ] = rank

            rank += 1

        logger.info(
            "Candidates ranked"
        )

        return ranked