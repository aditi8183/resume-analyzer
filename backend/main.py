from fastapi import FastAPI
from models.user import User
from models.user import User
from models.job_model import Job
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from database.database import Base, engine
from candidate.candidate_routes import router as candidate_router
from routes.auth_routes import router as auth_router
from routes.ats_routes import router as ats_router
from routes.job_routes import (
    router as job_router
)
Base.metadata.create_all(bind=engine)

app = FastAPI(

    title="Resume Analyzer ATS",

    version="1.0.0"

)
app.mount(
    "/resumes",
    StaticFiles(directory="uploads/resumes"),
    name="resumes"
)


app.add_middleware(

    CORSMiddleware,

    allow_origins=[

        "http://localhost:5173",

        "http://127.0.0.1:5173"

    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)


app.include_router(

    ats_router

)
app.include_router(auth_router)
app.include_router(
    job_router
)
app.include_router(candidate_router)

@app.get("/")
def home():

    return {

        "message":
            "ATS API Running"

    }