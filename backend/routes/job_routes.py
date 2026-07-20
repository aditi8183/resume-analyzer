print("JOB ROUTES LOADED")
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_db

from schemas.job_schema import (
    JobCreate,
    JobResponse
)

from crud.job_crud import JobCRUD

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


@router.post(
    "/create",
    response_model=JobResponse
)
def create_job(
    job: JobCreate,
    db: Session = Depends(get_db)
):

    return JobCRUD.create_job(
        db,
        job.title,
        job.description,
        job.required_skills,
        recruiter_id=1
    )


@router.get(
    "/",
    response_model=list[JobResponse]
)
def get_jobs(
    db: Session = Depends(get_db)
):

    return JobCRUD.get_all_jobs(db)