from phase5.json_exporter import (
    JSONExporter
)

from phase5.csv_exporter import (
    CSVExporter
)

from phase5.report_generator import (
    ReportGenerator
)

sample = {

    "scores": {

        "skill_score": 80,

        "keyword_score": 75,

        "experience_score": 100,

        "ats_score": 85
    },

    "matching": {

        "matched_skills": [

            "python",
            "sql"
        ]
    },

    "gaps": {

        "missing_skills": [

            "aws"
        ],

        "critical_missing": [

            "aws"
        ],

        "experience_gap": 0
    },

    "job_level": "Mid",

    "recommendations": [

        "Critical skill missing: aws"
    ]
}

JSONExporter.export(

    sample,

    "outputs/report.json"

)

CSVExporter.export(

    sample,

    "outputs/report.csv"

)

ReportGenerator.generate(

    sample,

    "outputs/report.txt"

)

print(
    "Phase 5 working"
)