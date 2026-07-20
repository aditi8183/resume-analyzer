from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey
)

from database.database import Base

from datetime import datetime


class Job(Base):

    __tablename__ = "jobs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String,
        nullable=False
    )

    description = Column(
        Text,
        nullable=False
    )

    required_skills = Column(
        Text,
        nullable=True
    )

    recruiter_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )