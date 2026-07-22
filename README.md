

## Project Title

**AI-Powered Hiring Assisstant and Resume Analyzer**

---

# 1. Abstract

Recruitment has become increasingly challenging due to the large volume of resumes received for every job opening. Manual screening of resumes is time-consuming and prone to inconsistencies. This project presents an AI-Powered  Resume Analyzer that automates resume screening, candidate-job matching, skill gap analysis, and candidate ranking.

The system enables recruiters to upload job descriptions and automatically evaluate uploaded resumes against job requirements. It extracts candidate information, identifies matching skills, highlights missing skills, calculates similarity scores, and ranks applicants based on their suitability for the role.

The platform provides separate dashboards for recruiters and candidates, allowing recruiters to manage candidate evaluations while candidates can upload resumes and view detailed analysis reports.

---

# 2. Problem Statement

Traditional recruitment processes suffer from:

* Manual resume screening consuming significant time.
* Difficulty in identifying the most relevant candidates.
* Human bias during candidate selection.
* Lack of detailed feedback for applicants.
* Challenges in handling large-scale recruitment.

An automated ATS system is required to streamline candidate evaluation and improve recruitment efficiency.

---

# 3. Objectives

The primary objectives of this project are:

1. Automate resume screening.
2. Extract candidate information from resumes.
3. Match resumes against job descriptions.
4. Calculate candidate-job compatibility scores.
5. Identify missing skills.
6. Rank candidates based on performance.
7. Provide recruiter and candidate dashboards.
8. Improve recruitment efficiency and accuracy.

---

# 4. Scope of the Project

The system focuses on:

* Resume parsing
* Skill extraction
* Job description analysis
* Resume-job matching
* Candidate ranking
* Gap analysis
* Recruiter management
* Candidate application management

Future versions can include interview scheduling, email notifications, and advanced AI recommendations

---

# 5. Technology Stack

## Frontend

* React.js
* TypeScript
* Vite
* Tailwind CSS
* React Router

## Backend

* Python
* FastAPI
* SQLAlchemy
* Pydantic

## Database

* SQLite

## AI / NLP Components

* Sentence Transformers
* Skill Matching Engine
* Similarity Scoring Module

## Resume Processing

* PyMuPDF
* PDFPlumber
* PyPDF2
* PDFMiner

---

# 6. System Architecture

The system follows a client-server architecture.

### Frontend Layer

Responsible for:

* User Authentication
* Recruiter Dashboard
* Candidate Dashboard
* Result Visualization

### Backend Layer

Responsible for:

* API Services
* Resume Processing
* Job Matching
* Ranking Logic
* Database Operations

### Database Layer

Stores:

* Users
* Recruiters
* Candidates
* Job Descriptions
* Applications
* Scores

---

# 7. Functional Modules

## Module 1: Authentication System

Features:

* User Registration
* Login
* Role-Based Access

Roles:

* Recruiter
* Candidate

---

## Module 2: Job Management

Recruiters can:

* Create jobs
* View jobs
* Manage job requirements

Stored information:

* Job Title
* Description
* Required Skills
* Experience Requirements

---

## Module 3: Resume Upload

Candidates can:

* Upload PDF resumes
* Apply for available jobs

Supported format:

* PDF

---

## Module 4: Resume Parsing

The parser extracts:

* Candidate Name
* Skills
* Education
* Experience
* Certifications

Libraries used:

* PyMuPDF
* PDFPlumber
* PDFMiner

---

## Module 5: Skill Extraction

The system identifies:

* Technical Skills
* Programming Languages
* Frameworks
* Tools

Examples:

* Python
* SQL
* Machine Learning
* React
* FastAPI

---

## Module 6: Job Matching Engine

The engine compares:

Resume Skills

vs

Job Required Skills

Outputs:

* Matching Skills
* Missing Skills
* Match Percentage

---

## Module 7: Ranking System

Candidates are ranked based on:

* Skill Match
* Semantic Similarity
* Experience Relevance

Final Score Formula:

Final Score = Skill Match + Similarity Score + Experience Score

---

## Module 8: Gap Analysis

The system identifies:

* Missing Skills
* Weak Areas
* Improvement Suggestions

Example:

Required:
Python, SQL, Machine Learning

Candidate:
Python, SQL

Missing:
Machine Learning

---

## Module 9: Result Dashboard

### Candidate Dashboard

Displays:

* Match Percentage
* Missing Skills
* Resume Analysis

### Recruiter Dashboard

Displays:

* Applicant Rankings
* Candidate Scores
* Candidate Reports

---

# 8. Database Design

## Users Table

| Field    | Description         |
| -------- | ------------------- |
| id       | User ID             |
| username | Username            |
| password | Password            |
| role     | Recruiter/Candidate |

---

## Jobs Table

| Field           | Description     |
| --------------- | --------------- |
| id              | Job ID          |
| title           | Job Title       |
| description     | Job Description |
| required_skills | Required Skills |

---

## Applications Table

| Field        | Description    |
| ------------ | -------------- |
| id           | Application ID |
| candidate_id | Candidate      |
| job_id       | Applied Job    |
| score        | ATS Score      |

---

# 9. Workflow

### Recruiter Workflow

1. Login
2. Create Job
3. View Applications
4. Analyze Rankings
5. Select Candidates

### Candidate Workflow

1. Login
2. View Jobs
3. Upload Resume
4. Apply
5. View Analysis Report

---

# 10. Results Achieved

The system successfully:

* Parses PDF resumes.
* Extracts skills.
* Matches resumes against jobs.
* Calculates ATS scores.
* Identifies missing skills.
* Ranks candidates.
* Provides recruiter and candidate dashboards.

---

# 11. Advantages

* Reduces manual screening effort.
* Faster candidate evaluation.
* Improved recruitment accuracy.
* Skill gap identification.
* Scalable architecture.
* User-friendly dashboards.

---

# 12. Limitations

* Supports only PDF resumes.
* Limited domain-specific skill database.
* No interview scheduling integration.
* No email notification system.
* Does not facilitate real endpoints for job creation on recruiters end
* No endpoints for candidate resume to reach recruiter dashboard automatically
---

# 13. Future Enhancements

1. AI-based interview recommendations.
2. Resume improvement suggestions.
3. Email notifications.
4. Cloud deployment.
5. Advanced NLP skill extraction.
6. Interview scheduling module.
7. Analytics dashboard.
8. Multi-company support.

---

# 14. Conclusion

The AI-Powered Resume Analyzer and Ranking System successfully automates key recruitment tasks such as resume screening, skill extraction, job matching, candidate ranking, and skill gap analysis. The system reduces recruitment effort while improving candidate selection accuracy. With future enhancements, it can evolve into a complete intelligent recruitment platform suitable for real-world hiring environments.

---

## GitHub Repository

Repository URL:

`https://github.com/aditi8183/resume-analyzer`


## Installation

### Clone Repository 

git clone https://github.com/aditi8183/resume-analyzer.git
cd resume-analyzer

### Create Virtual Environment

python -m venv venv

Activate:


Windows:

venv\Scripts\activate


Linux/Mac:

source venv/bin/activate


### Install Dependencies


pip install -r requirements.txt


## Run Backend

Navigate to backend folder:

cd backend


Run:

uvicorn app:app --reload


Backend URL:


http://localhost:8000
Swagger Documentation:


http://localhost:8000/docs

## Run Frontend

Navigate to frontend folder:

cd frontend


Install packages:

npm install


Run:

npm run dev


Frontend URL:

http://localhost:5173


## Author

Aditi Ansh
