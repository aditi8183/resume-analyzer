from sqlalchemy.orm import Session

from models.user import User

from utils.security import (

    hash_password,

    verify_password
)


class UserCRUD:

    @staticmethod
    def get_by_email(

        db: Session,

        email: str

    ):

        return (

            db.query(User)

            .filter(
                User.email == email
            )

            .first()
        )

    @staticmethod
    def create_user(

        db: Session,

        name,

        email,

        password,

        role

    ):

        user = User(

            name=name,

            email=email,

            password=hash_password(
                password
            ),

            role=role
        )

        db.add(user)

        db.commit()

        db.refresh(user)

        return user

    @staticmethod
    def authenticate_user(

        db: Session,

        email,

        password

    ):

        user = (

            db.query(User)

            .filter(
                User.email == email
            )

            .first()
        )

        if not user:

            return None

        if not verify_password(

            password,

            user.password

        ):

            return None

        return user