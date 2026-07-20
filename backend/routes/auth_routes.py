from fastapi import (

    APIRouter,

    Depends,

    HTTPException
)

from sqlalchemy.orm import (
    Session
)

from schemas.user_schema import (

    UserCreate,

    UserResponse,

    UserLogin
)

from crud.user_crud import (
    UserCRUD
)

from database.database import (
    get_db
)

from auth.jwt_handler import (
    create_access_token
)

router = APIRouter(

    prefix="/auth",

    tags=["Authentication"]
)


@router.get("/test")
def test():

    return {

        "message":

            "Auth Route Working"
    }


@router.post(

    "/register",

    response_model=UserResponse
)
def register(

    user: UserCreate,

    db: Session = Depends(
        get_db
    )
):

    existing_user = (

        UserCRUD
        .get_by_email(

            db,

            user.email
        )

    )

    if existing_user:

        raise HTTPException(

            status_code=400,

            detail="Email already registered"
        )

    created_user = (

        UserCRUD
        .create_user(

            db,

            user.name,

            user.email,

            user.password,

            user.role
        )

    )

    return created_user


@router.post("/login")
def login(

    credentials: UserLogin,

    db: Session = Depends(
        get_db
    )
):

    user = (

        UserCRUD
        .authenticate_user(

            db,

            credentials.email,

            credentials.password
        )

    )

    if not user:

        raise HTTPException(

            status_code=401,

            detail="Invalid email or password"
        )

    token = create_access_token(

        {

            "user_id": user.id,

            "email": user.email,

            "role": user.role
        }

    )

    return {

        "access_token":

            token,

        "token_type":

            "bearer",

        "user_id":

            user.id,

        "name":

            user.name,

        "email":

            user.email,

        "role":

            user.role
    }