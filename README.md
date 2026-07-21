# AI-Powered Resume Analyzer & ATS System

## Overview

This project is an AI-powered Smart Hiring Assisstant and Resume Analyzer developed as an academic capstone project.

The system analyzes resumes against job descriptions and provides:
* Resume parsing
* Job description parsing
* ATS Score
* Skill Match Score
* Keyword Match Score
* Education Match Score
* Experience Match Score
* Semantic Similarity Analysis
* Candidate Ranking
* Recruiter Dashboard
* Candidate Dashboard

The goal is to simulate a real-world ATS workflow used by recruiters for resume screening and candidate shortlisting.

---

## Project Architecture

### Phase 1 – Resume Extraction

Extracts text from PDF resumes using:

* PyMuPDF
* PDFPlumber
* OCR fallback for scanned resumes

---

### Phase 2 – Layout Parsing

Organizes extracted text into logical resume sections such as:

* Skills
* Education
* Experience
* Projects
* Certifications

---

### Phase 3 – Information Extraction

Extracts structured candidate information:

* Candidate Name
* Skills
* Keywords
* Education
* Experience
* Projects
* Certifications

A skill ontology is used to expand related skills.

Example:

```txt
Python → Programming
Machine Learning → AI
```

---

### Phase 4 – ATS Matching Engine

Matches resume content against the job description.

Scores generated:

* Skill Score
* Keyword Score
* Experience Score
* Education Score
* Certification Score

These are combined into an overall ATS score.

---

### Phase 5 – Candidate Ranking

Candidates are ranked against each job description based on ATS score and matching metrics.

---

### Phase 6 – Semantic Analysis

Uses transformer-based embeddings to evaluate semantic similarity between:

* Resume
* Job Description

This allows identification of relevant candidates even when exact keywords differ.

---

### Phase 7 – Explainability Engine

Generates explanations for:

* Matched skills
* Missing skills
* Strengths
* Weaknesses
* Hiring recommendations

---

## Recruiter Module

Recruiters can:

* Create accounts
* Log in
* Post jobs
* Upload resumes
* View ATS scores
* View ranked candidates
* Review candidate profiles

---

## Candidate Module

Candidates can:

* Register
* Log in
* Upload resumes
* Apply to jobs
* View ATS analysis results

---

## Technology Stack

### Backend

* FastAPI
* SQLAlchemy
* SQLite
* Uvicorn
* JWT Authentication

### AI / NLP

* Sentence Transformers
* Transformers
* Scikit-learn

### Resume Processing

* PyMuPDF
* PDFPlumber
* PDFMiner
* PaddleOCR

### Frontend

* React
* Vite

---

## Installation

### Clone Repository

```bash
git clone https://github.com/aditi8183/resume-analyzer.git
cd resume-analyzer
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Backend

Navigate to backend folder:

```bash
cd backend
```

Run:

```bash
uvicorn app:app --reload
```

Backend URL:

```txt
http://localhost:8000
```

Swagger Documentation:

```txt
http://localhost:8000/docs
```

---

## Run Frontend

Navigate to frontend folder:

```bash
cd frontend
```

Install packages:

```bash
npm install
```

Run:

```bash
npm run dev
```

Frontend URL:

```txt
http://localhost:5173
```

---

## Key Features

✔ Resume Parsing

✔ OCR Support

✔ ATS Scoring

✔ Semantic Matching

✔ Candidate Ranking

✔ Recruiter Dashboard

✔ Candidate Dashboard

✔ Job Posting System

✔ Authentication & Authorization

---

## Future Improvements

* PostgreSQL Integration
* Cloud Deployment
* Advanced Resume Parsing
* Interview Recommendation Engine
* Actual endpoint creation for job create option on recruiter dashboard , this same created job should reach the candidate dashboard under available jobs and then candidates may apply
* AI Resume Improvement Suggestions

---

## Academic Use

This project was developed as an academic capstone project to demonstrate practical implementation of:

* FastAPI
* NLP
* Machine Learning
* Resume Parsing
* ATS Design
* Full Stack Development

---

## Author

Aditi Ansh
