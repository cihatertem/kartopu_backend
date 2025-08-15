import uuid
from sqlmodel import SQLModel, Field
from pydantic import ConfigDict, EmailStr


class UserBase(SQLModel):
    first_name: str = Field(min_length=2, max_length=22)
    last_name: str = Field(min_length=2, max_length=22)
    username: str = Field(index=True, unique=True, min_length=2, max_length=15)
    # hashed_password: str
    email: EmailStr = Field(unique=True)


class UserResponse(UserBase):
    id: uuid.UUID


class UserCreate(UserBase):
    model_config = ConfigDict(extra="forbid")  # type: ignore reportIncompatibleVariableOverride


class UserUpdate(SQLModel):
    first_name: str | None = None
    last_name: str | None = None
    username: str | None = None
    email: EmailStr | None = None

    model_config = ConfigDict(extra="forbid")  # pyright: ignore reportIncompatibleVariableOverride
