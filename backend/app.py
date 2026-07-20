import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from database.database import (
    Base,
    engine
)
from fastapi.middleware.cors import CORSMiddleware
from models.user import (
    User
)
from models.job_model import (
    Job
)

from routes.auth_routes import (
    router as auth_router
)

from recruiter.recruiter_routes import (
    router as recruiter_router
)

from candidate.candidate_routes import (
    router as candidate_router
)

from routes.ats_routes import (
    router as ats_router
)

# ==========================
# Create Database Tables
# ==========================

Base.metadata.create_all(
    bind=engine
)

# ==========================
# FastAPI App
# ==========================

app = FastAPI(

    title="AI ATS Platform",

    version="1.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
print("CURRENT DIR:", os.getcwd())
print("RESUME PATH EXISTS:", os.path.exists("uploads/resumes"))

app.mount(

    "/resumes",

    StaticFiles(
        directory="uploads/resumes"
    ),

    name="resumes"

)

# ==========================
# Routers
# ==========================

app.include_router(
    auth_router
)

app.include_router(
    recruiter_router
)

app.include_router(
    candidate_router
)

app.include_router(
    ats_router
)

# ==========================
# Home Route
# ==========================

@app.get("/")
def home():

    return {

        "message":

            "ATS Backend Running"
    }