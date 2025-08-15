from typing import TYPE_CHECKING
import uuid
from sqlmodel import Field, Relationship

from app.schemas.user import UserBase

if TYPE_CHECKING:
    from app.models.post import Post


class User(UserBase, table=True):
    __tablename__ = "users"  # type: ignore[reportAssignmentType]
    id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    is_admin: bool = Field(default=False)
    is_active: bool = Field(default=False)

    posts: list["Post"] = Relationship(back_populates="author", cascade_delete=True)
