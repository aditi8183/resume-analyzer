from models.job_model import Job


class JobCRUD:

    @staticmethod
    def create_job(

        db,

        title,

        description,

        required_skills,

        recruiter_id

    ):

        job = Job(

            title=title,

            description=description,

            required_skills=required_skills,

            recruiter_id=recruiter_id

        )

        db.add(job)

        db.commit()

        db.refresh(job)

        return job

    @staticmethod
    def get_all_jobs(db):

        return db.query(Job).all()