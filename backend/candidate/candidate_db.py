import sqlite3
import json
import os
from datetime import datetime

DB_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "ats.db"
)


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_id INTEGER NOT NULL,
            candidate_name TEXT NOT NULL,
            resume_path TEXT NOT NULL,
            resume_url TEXT,

            final_score REAL,
            ats_score REAL,
            skill_score REAL,
            semantic_score REAL,

            strengths TEXT,
            weaknesses TEXT,

            matched_skills TEXT,
            missing_skills TEXT,

            status TEXT DEFAULT 'Submitted',
            submitted_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_application(
    job_id,
    candidate_name,
    resume_path,
    resume_url,
    result
):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO applications (
            job_id,
            candidate_name,
            resume_path,
            resume_url,
            final_score,
            ats_score,
            skill_score,
            semantic_score,
            strengths,
            weaknesses,
            matched_skills,
            missing_skills,
            status,
            submitted_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        job_id,
        candidate_name,
        resume_path,
        resume_url,

        result.get("final_score"),
        result.get("ats_score"),
        result.get("skill_score"),
        result.get("semantic_score"),

        json.dumps(result.get("strengths", [])),
        json.dumps(result.get("weaknesses", [])),

        json.dumps(result.get("matched_skills", [])),
        json.dumps(result.get("missing_skills", [])),

        "Submitted",
        datetime.utcnow().isoformat()
    ))

    conn.commit()

    application_id = cur.lastrowid

    conn.close()

    return application_id


def _row_to_application(row):
    data = dict(row)

    data["strengths"] = json.loads(
        data["strengths"] or "[]"
    )

    data["weaknesses"] = json.loads(
        data["weaknesses"] or "[]"
    )

    data["matched_skills"] = json.loads(
        data["matched_skills"] or "[]"
    )

    data["missing_skills"] = json.loads(
        data["missing_skills"] or "[]"
    )

    return data


def get_application(application_id):
    conn = get_connection()

    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM applications WHERE id=?",
        (application_id,)
    )

    row = cur.fetchone()

    conn.close()

    if row:
        return _row_to_application(row)

    return None

def get_job(job_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM jobs WHERE id = ?",
        (job_id,)
    )

    row = cur.fetchone()

    conn.close()

    return dict(row) if row else None
def list_all_applications():
    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""
        SELECT *
        FROM applications
        ORDER BY submitted_at DESC
    """)

    rows = cur.fetchall()

    conn.close()

    return [
        _row_to_application(row)
        for row in rows
    ]


init_db()
 