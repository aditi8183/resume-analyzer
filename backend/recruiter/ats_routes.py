from fastapi import (
    APIRouter,
    UploadFile,
    File
)

from services.ats_pipeline import (
    ATSPipeline
)

router = APIRouter(
    prefix="/ats",
    tags=["ATS"]
)


@router.get("/test")
def ats_test():

    result = ATSPipeline.run(
        "../cv (1).pdf",
        "../sample_data_scientist_jd.pdf"
    )

    return result


@router.post("/upload")
async def upload_and_analyze(

    resume: UploadFile = File(...),

    jd: UploadFile = File(...)
):

    resume_path = f"uploads/{resume.filename}"
    jd_path = f"uploads/{jd.filename}"

    with open(
        resume_path,
        "wb"
    ) as f:

        f.write(
            await resume.read()
        )

    with open(
        jd_path,
        "wb"
    ) as f:

        f.write(
            await jd.read()
        )

    result = ATSPipeline.run(
        resume_path,
        jd_path
    )

    return result