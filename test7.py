from phase7.candidate_ranker import (
    CandidateRanker
)

candidates = [

    {

        "name":
            "Alice",

        "ats_score":
            90,

        "semantic_score":
            92,

        "fit_score":
            95
    },

    {

        "name":
            "Bob",

        "ats_score":
            85,

        "semantic_score":
            80,

        "fit_score":
            88
    },

    {

        "name":
            "Charlie",

        "ats_score":
            95,

        "semantic_score":
            90,

        "fit_score":
            90
    }
]

result = (

    CandidateRanker
    .rank(
        candidates
    )

)

for candidate in result:

    print(

        candidate[
            "rank"
        ],

        candidate[
            "name"
        ],

        candidate[
            "final_score"
        ]

    )