from fastapi import (

    APIRouter,

    Depends
)

from dependencies.auth_dependency import (

    recruiter_required
)

router = APIRouter(

    prefix="/recruiter",

    tags=["Recruiter"]
)


@router.get("/dashboard")
def recruiter_dashboard(

    user=Depends(
        recruiter_required
    )
):

    return {

        "message":

            "Recruiter Dashboard",

        "user":

            user
    }