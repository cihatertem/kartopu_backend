import uuid
from sqlmodel import Field

from app.schemas.user import UserBase
# from app.db.session import SQLModel


class User(UserBase, table=True):
    id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    is_admin: bool = Field(default=False)
    is_active: bool = Field(default=False)
