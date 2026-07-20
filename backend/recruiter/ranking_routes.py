from fastapi import (
    APIRouter,
    UploadFile,
    File
)

from services.ats_pipeline import (
    ATSPipeline
)

router = APIRouter(

    prefix="/ranking",

    tags=["Ranking"]
)


@router.post("/rank")
async def rank_candidates(

    jd: UploadFile = File(...),

    resumes: list[UploadFile] = File(...)
):

    jd_path = f"uploads/{jd.filename}"

    with open(

        jd_path,

        "wb"

    ) as f:

        f.write(

            await jd.read()
        )

    results = []

    for resume in resumes:

        resume_path = (

            f"uploads/{resume.filename}"
        )

        with open(

            resume_path,

            "wb"

        ) as f:

            f.write(

                await resume.read()
            )

        ats_result = (

            ATSPipeline.run(

                resume_path,

                jd_path

            )
        )

        results.append({

            "resume":

                resume.filename,

            "ats_score":

                ats_result[
                    "result"
                ][
                    "scores"
                ][
                    "ats_score"
                ],

            "fit_level":

                ats_result[
                    "result"
                ][
                    "scores"
                ][
                    "fit_level"
                ]
        })

    results.sort(

        key=lambda x:

            x["ats_score"],

        reverse=True
    )

    rank = 1

    for candidate in results:

        candidate[
            "rank"
        ] = rank

        rank += 1

    return results