from fastapi import (

    Depends,

    HTTPException
)

from fastapi.security import (

    OAuth2PasswordBearer
)

from jose import (

    jwt,

    JWTError
)

from auth.jwt_handler import (

    SECRET_KEY,

    ALGORITHM
)

oauth2_scheme = OAuth2PasswordBearer(

    tokenUrl="auth/login"
)


def get_current_user(

    token: str = Depends(
        oauth2_scheme
    )
):

    try:

        payload = jwt.decode(

            token,

            SECRET_KEY,

            algorithms=[ALGORITHM]
        )

        return payload

    except JWTError:

        raise HTTPException(

            status_code=401,

            detail="Invalid Token"
        )


def recruiter_required(

    user=Depends(
        get_current_user
    )
):

    if user["role"] != "recruiter":

        raise HTTPException(

            status_code=403,

            detail="Recruiter Access Only"
        )

    return user


def candidate_required(

    user=Depends(
        get_current_user
    )
):

    if user["role"] != "candidate":

        raise HTTPException(

            status_code=403,

            detail="Candidate Access Only"
        )

    return user