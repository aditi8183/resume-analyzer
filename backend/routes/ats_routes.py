from fastapi import (
    APIRouter,
    UploadFile,
    File
)

from typing import Annotated

from services.ats_pipeline import (
    ATSPipeline
)

from phase7.candidate_ranker import (
    CandidateRanker
)

from phase7_3.candidate_loader import (
    CandidateLoader
)

from phase7_3.bulk_processor import (
    BulkProcessor
)

from jd.jd_parser import (
    JDParser
)

import shutil
import os


router = APIRouter(

    prefix="/ats",

    tags=["ATS"]

)


UPLOAD_DIR = "uploads"

LAST_RESUME = None
LAST_JD = None


@router.get("/")
def ats_home():

    return {

        "message":
            "ATS Route Working"

    }


# ======================================
# SINGLE UPLOAD
# ======================================

@router.post("/upload")
def upload_files(

    resume: UploadFile = File(...),

    jd: UploadFile = File(...)

):

    global LAST_RESUME
    global LAST_JD

    os.makedirs(

        UPLOAD_DIR,

        exist_ok=True

    )

    resume_path = (

        f"{UPLOAD_DIR}/{resume.filename}"

    )

    jd_path = (

        f"{UPLOAD_DIR}/{jd.filename}"

    )

    with open(

        resume_path,

        "wb"

    ) as buffer:

        shutil.copyfileobj(

            resume.file,

            buffer

        )

    with open(

        jd_path,

        "wb"

    ) as buffer:

        shutil.copyfileobj(

            jd.file,

            buffer

        )

    LAST_RESUME = resume_path
    LAST_JD = jd_path

    return {

        "resume_saved":
            resume_path,

        "jd_saved":
            jd_path,

        "message":
            "Files uploaded successfully"

    }


# ======================================
# BULK UPLOAD
# ======================================

@router.post("/upload-bulk")
async def upload_bulk_files(

    jd: Annotated[UploadFile, File(...)],

    resumes: Annotated[list[UploadFile], File(...)]

):

    os.makedirs(

        "uploads/jd",

        exist_ok=True

    )

    os.makedirs(

        "uploads/resumes",

        exist_ok=True

    )
    for file in os.listdir("uploads/resumes"):
        os.remove(
            os.path.join(
                "uploads/resumes",
                file
            )
        )
    for file in os.listdir("uploads/jd"):
        os.remove(
            os.path.join(
                "uploads/jd",
                file
            )
        )

    jd_path = (

        f"uploads/jd/{jd.filename}"

    )

    with open(

        jd_path,

        "wb"

    ) as buffer:

        shutil.copyfileobj(

            jd.file,

            buffer

        )

    saved_resumes = []

    for resume in resumes:

        resume_path = (

            f"uploads/resumes/{resume.filename}"

        )

        with open(

            resume_path,

            "wb"

        ) as buffer:

            shutil.copyfileobj(

                resume.file,

                buffer

            )

        saved_resumes.append(

            resume.filename

        )

    return {

        "message":
            "Bulk upload successful",

        "jd":
            jd.filename,

        "resume_count":
            len(saved_resumes),

        "resumes":
            saved_resumes

    }


# ======================================
# SINGLE ANALYSIS
# ======================================

@router.post("/analyze")
def analyze_resume():

    global LAST_RESUME
    global LAST_JD

    if (

        LAST_RESUME is None

        or

        LAST_JD is None

    ):

        return {

            "error":
                "Upload resume and JD first"

        }

    output = (

        ATSPipeline.run(

            LAST_RESUME,

            LAST_JD

        )

    )

    return output


# ======================================
# BULK RANKING
# ======================================

@router.post("/bulk-rank")
def bulk_rank_candidates():

    resume_files = (

        CandidateLoader.load(

            "uploads/resumes"

        )

    )

    if len(resume_files) == 0:

        return {

            "error":
                "No resumes found"

        }

    jd_folder = "uploads/jd"

    jd_files = [

        f for f in os.listdir(jd_folder)

        if f.endswith(".pdf")

    ]

    if len(jd_files) == 0:

        return {

            "error":
                "No JD uploaded"

        }

    jd_path = os.path.join(

        jd_folder,

        jd_files[0]

    )

    jd_profile = (

        JDParser()
        .parse(

            jd_path

        )

    )
    jd_summary = {

    "job_title": "Uploaded Job Description",

    "experience_required": jd_profile.get(
        "experience",
        "Not specified"
    ),

    "required_skills": jd_profile.get(
        "skills",
        []
    ),

    "critical_skills": jd_profile.get(
        "skills",
        []
    )[:5]

    }

    processed = (

        BulkProcessor.process(

            resume_files,

            jd_profile

        )

    )
    print("RESUME FILES:", resume_files)
    print("PROCESSED COUNT:", len(processed))

    candidates = []

    for item in processed:

        result = item["result"]

        semantic = result["semantic"]

        phase4 = result["result"]

        explanation = result.get(

            "explanation",

            {}

        )
        print("\nRESUME PROFILE:")
        print(result["resume_profile"])

        print(
            "RESUME:",
              os.path.basename(item["resume"])
        )

        print(
            "EDUCATION:",
              result["result"]["matching"]["matched_degree"]
        )
        print(
            "PHASE4 SCORES:",
              phase4["scores"]
        )

        candidates.append (

           {

                "name":
                   result["resume_profile"].get(
                     "name",
                     os.path.basename(item["resume"])
                   ),
                
                "resume_url":
                    item["resume_url"],
                    

                "ats_score":

                    phase4["scores"]["ats_score"],
                "fit_category":
                   semantic.get(
                       "fit_category",
                        "Unknown"
                    ),
                "hiring_recommendation":
                    semantic.get(
                       "hiring_recommendation",
                       "Needs Further Review"
                    ),

                "skill_score":
                    phase4["scores"]["skill_score"],
                "keyword_score":
                    phase4["scores"]["keyword_score"],

                "semantic_score":

                    semantic["semantic_score"],

                "fit_score":

                    semantic["fit_score"],

                "project_score":

                    semantic.get(

                        "project_score",

                        0

                    ),

                "experience_relevance_score":

                    semantic.get(

                        "experience_relevance_score",

                        0

                    ),

                "education_score":

                    phase4["scores"].get(

                        "education_score",

                        0

                    ),

                "certification_score":

                    phase4["scores"].get(

                        "certification_score",

                        0

                    ),

                "strengths":

                    explanation.get(

                        "strengths",

                        []

                    ),

                "weaknesses":

                    explanation.get(

                        "weaknesses",

                        []

                    ),
                "matched_skills":

                    phase4["matching"].get(

                      "matched_skills",
      
                       []

                    ),

                "missing_skills":

                    phase4["gaps"].get(

                      "missing_skills",

                        []

                    ),

                "critical_missing":

                    phase4["gaps"].get(

                        "critical_missing",

                        []

                    ),

            }

        )
    print(candidates[0])

    ranked = CandidateRanker.rank(candidates)

    
    jd_summary = {
    "job_title": jd_profile.get("job_title", ""),
    "experience_required": jd_profile.get("experience_required", ""),
    "required_skills": jd_profile.get("required_skills", []),
    "critical_skills": jd_profile.get("critical_skills", [])
    }

    return {
    "jd_summary": jd_summary,
    "candidates": ranked
    }