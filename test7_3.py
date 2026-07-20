from phase7_3.shortlist_engine import (
    ShortlistEngine
)

from phase7_3.recruiter_summary import (
    RecruiterSummary
)

candidates = [

    {
        "name": "Alice",
        "ats_score": 92
    },

    {
        "name": "Bob",
        "ats_score": 65
    },

    {
        "name": "Charlie",
        "ats_score": 81
    }
]

result = (

    ShortlistEngine
    .shortlist(

        candidates,

        threshold=75

    )

)

summary = (

    RecruiterSummary
    .generate(

        candidates

    )

)

print(result)

print()

print(summary)