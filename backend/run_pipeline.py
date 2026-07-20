import sys

from phase1.resume_extractor import (
    ResumeExtractor
)

from phase2.layout_parser import (
    LayoutParser
)

from phase3.phase_parser import (
    Phase3Parser
)

from jd.jd_parser import (
    JDParser
)

from phase4.matcher import (
    Matcher
)

from phase5.json_exporter import (
    JSONExporter
)

from phase5.csv_exporter import (
    CSVExporter
)

from phase5.report_generator import (
    ReportGenerator
)

from logger import logger


def main():

    if len(sys.argv) != 3:

        print(
            "Usage: python main.py <resume_file> <jd_file>"
        )

        return

    resume_file = sys.argv[1]

    jd_file = sys.argv[2]

    logger.info(
        "Starting ATS pipeline"
    )

    # ==========================
    # Phase 1
    # ==========================

    phase1_output = (

        ResumeExtractor()
        .extract(
            resume_file
        )

    )

    # ==========================
    # Phase 2
    # ==========================

    phase2_output = (

        LayoutParser()
        .parse(
            phase1_output
        )

    )

    # ==========================
    # Phase 3
    # ==========================

    resume_profile = (

        Phase3Parser()
        .parse(
            phase2_output
        )

    )

    # ==========================
    # JD Parsing
    # ==========================

    jd_profile = (

        JDParser()
        .parse(
            jd_file
        )

    )

    # ==========================
    # Phase 4
    # ==========================

    result = (

        Matcher()
        .match(

            resume_profile,

            jd_profile

        )

    )

    # ==========================
    # Phase 5
    # ==========================

    JSONExporter.export(

        result,

        "outputs/report.json"

    )

    CSVExporter.export(

        result,

        "outputs/report.csv"

    )

    ReportGenerator.generate(

        result,

        "outputs/report.txt"

    )

    print(
        "\nATS Score:",
        result[
            "scores"
        ][
            "ats_score"
        ]
    )

    print(
        "\nJob Level:",
        result[
            "job_level"
        ]
    )

    print(
        "\nMatched Skills:"
    )

    for skill in result[
        "matching"
    ][
        "matched_skills"
    ]:

        print(
            "-",
            skill
        )

    print(
        "\nMissing Skills:"
    )

    for skill in result[
        "gaps"
    ][
        "missing_skills"
    ]:

        print(
            "-",
            skill
        )

    print(
        "\nCritical Missing Skills:"
    )

    for skill in result[
        "gaps"
    ][
        "critical_missing"
    ]:

        print(
            "-",
            skill
        )

    print(
        "\nRecommendations:"
    )

    for recommendation in result[
        "recommendations"
    ]:

        print(
            "-",
            recommendation
        )

    print(
        "\nReports saved to outputs/"
    )

    logger.info(
        "Pipeline completed successfully"
    )


if __name__ == "__main__":

    main()