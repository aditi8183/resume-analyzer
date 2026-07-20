
import os
import shutil
import uuid
from database.database import get_db
from sqlalchemy.orm import Session
import traceback
from crud.job_crud import JobCRUD
from fastapi import Depends

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Form,
    HTTPException
)

from phase1.resume_extractor import ResumeExtractor
from phase2.layout_parser import LayoutParser
from phase3.phase_parser import Phase3Parser
from phase4.matcher import Matcher
from phase6.semantic_engine import SemanticEngine
from phase7.explanation_engine import ExplanationEngine
from jd.jd_parser import JDParser
from models.job_model import Job
from . import candidate_db as db


router = APIRouter(
    prefix="/candidate",
    tags=["Candidate"]
)


@router.get("/dashboard")
def candidate_dashboard():
    return {
        "message": "Candidate Dashboard Working"
    }


RESUME_UPLOAD_DIR = os.path.join(
    "uploads",
    "resumes"
)

os.makedirs(
    RESUME_UPLOAD_DIR,
    exist_ok=True
)

@router.get("/jobs")
def get_jobs(
    db_session: Session = Depends(get_db)
):
    jobs = JobCRUD.get_all_jobs(db_session)

    return jobs

@router.post("/apply")
async def apply_to_job(
    name: str = Form(...),
    job_id: int = Form(...),
    resume: UploadFile = File(...),
    db_session: Session = Depends(get_db)
):
    
    job = db_session.query(Job).filter(
        Job.id == job_id
    ).first()

    if not job:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )
    jd_profile = {
        "skills": [
            skill.strip()
            for skill in (job.required_skills or "").split(",")
            ] if job.required_skills else [],
        "keywords":  [
            skill.strip()
            for skill in job.required_skills.split(",")
            ] if job.required_skills else [],

        "experience": 0,
        "text": job.description,
        "required_skills": [
            skill.strip()
            for skill in (job.required_skills or "").split(",")
            ] if job.required_skills else [],
        "critical_skills": [
            skill.strip()
            for skill in (job.required_skills or "").split(",")
            ][:5] if job.required_skills else []
    }
    print("JD PROFILE")
    print(jd_profile)
    file_ext = os.path.splitext(
        resume.filename
    )[1]

    saved_filename = (
        f"{uuid.uuid4().hex}{file_ext}"
    )

    resume_path = os.path.join(
        RESUME_UPLOAD_DIR,
        saved_filename
    ) 
    
    with open(
        resume_path,
        "wb"
    ) as out_file:
        shutil.copyfileobj(
            resume.file,
            out_file
        )

    resume_url = (
        f"http://127.0.0.1:8000/resumes/{saved_filename}"
    )

    try:

        phase1_output = (
            ResumeExtractor()
            .extract(resume_path)
        )

        phase2_output = (
            LayoutParser()
            .parse(phase1_output)
        )

        resume_profile = (
            Phase3Parser()
            .parse(phase2_output)
        )
        print("FINAL JD PROFILE BEFORE MATCHER")
        print(jd_profile)

        phase4_result = (
            Matcher()
            .match(
                resume_profile,
                jd_profile
            )
        )

        semantic_result = (
            SemanticEngine()
            .analyze(
                resume_profile,
                jd_profile,
                phase4_result
            )
        )

        explanation = (
            ExplanationEngine.generate({
                **phase4_result["scores"],
                **semantic_result,
                "matched_skills":
                    phase4_result["matching"]["matched_skills"],
                "missing_skills":
                    phase4_result["gaps"]["missing_skills"],
                "critical_missing":
                    phase4_result["gaps"]["critical_missing"],
            })
        )

        result = {
            "final_score":
                semantic_result.get("fit_score"),

            "ats_score":
                phase4_result["scores"]["ats_score"],

            "skill_score":
                phase4_result["scores"]["skill_score"],

            "semantic_score":
                semantic_result["semantic_score"],

            "experience_relevance_score":
                semantic_result["experience_relevance_score"],

            "project_score":
                semantic_result["project_score"],

            "education_score":
                phase4_result["scores"]["education_score"],

            "certification_score":
                phase4_result["scores"]["certification_score"],

            "keyword_score":
                phase4_result["scores"]["keyword_score"],

            "fit_category":
                semantic_result["fit_category"],

            "hiring_recommendation":
                semantic_result["hiring_recommendation"],

            "strengths":
                explanation["strengths"],

            "weaknesses":
                explanation["weaknesses"],

            "matched_skills":
                phase4_result["matching"]["matched_skills"],

            "missing_skills":
                phase4_result["gaps"]["missing_skills"]
        }
    except Exception as e:

        traceback.print_exc()

        raise HTTPException(
        status_code=500,
        detail=f"Failed to process resume: {e}"
        )
    

    application_id = db.save_application(
        job_id=job_id,
        candidate_name=name,
        resume_path=resume_path,
        resume_url=resume_url,
        result=result
    )

    return {
        "application_id": application_id,
        "name": name,
        "job_title": job.title,
        **result
    }


@router.get("/application/{application_id}")
def get_application_result(
    application_id: int
):

    application = db.get_application(
        application_id
    )

    if not application:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    return application
