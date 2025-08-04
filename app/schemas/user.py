import uuid
from sqlmodel import SQLModel, Field
from pydantic import EmailStr


class UserBase(SQLModel):
    first_name: str = Field(min_length=2, max_length=22)
    last_name: str = Field(min_length=2, max_length=22)
    username: str = Field(index=True, unique=True, min_length=2, max_length=15)
    # hashed_password: str
    email: EmailStr = Field(unique=True)


class UserReponseBase(UserBase):
    id: uuid.UUID


class UserCreate(UserBase):
    class Config:  # pyright: ignore reportIncompatibleVariableOverride
        extra = "forbid"


class UserUpdate(SQLModel):
    first_name: str | None = None
    last_name: str | None = None
    username: str | None = None
    email: EmailStr | None = None

    class Config:  # pyright: ignore reportIncompatibleVariableOverride
        extra = "forbid"
