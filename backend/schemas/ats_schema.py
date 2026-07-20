from pydantic import BaseModel


class ATSResponse(BaseModel):

    resume_profile: dict

    jd_profile: dict

    result: dict