import uuid
from datetime import datetime, timezone
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship
from app.schemas.post import PostBase

if TYPE_CHECKING:
    from app.models.user import User


class Post(PostBase, table=True):
    __tablename__ = "posts"  # type: ignore[reportAssignmentType]
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), nullable=False
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        nullable=False,
        sa_column_kwargs={"onupdate": lambda: datetime.now(timezone.utc)},
    )

    author_id: uuid.UUID | None = Field(
        default=None, foreign_key="user.id", ondelete="CASCADE"
    )
    author: "User" | None = Relationship(back_populates="posts")  # type: ignore[ reportGeneralTypeIssues]
