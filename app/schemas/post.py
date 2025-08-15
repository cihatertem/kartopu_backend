import uuid
from datetime import datetime
from pydantic import ConfigDict
from sqlmodel import Field, SQLModel


class PostBase(SQLModel):
    title: str = Field(index=True, max_length=200, description="Blog post başlığı")
    slug: str = Field(
        index=True,
        unique=True,
        max_length=200,
        description="URL için düzenlenmiş başlık",
    )
    body: str | None = Field(default=None)
    summary: str | None = Field(default=None, max_length=500, description="Kısa özet")
    is_published: bool = Field(default=False, description="Yayınlanma durumu")


class PostCreate(PostBase):
    model_config = ConfigDict(extra="forbid")  # type: ignore[reportAssignmentType]


class PostResponse(PostBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    author_id: uuid.UUID


class PostUpdate(SQLModel):
    title: str | None = None
    slug: str | None = None
    body: str | None = None
    summary: str | None = None
    is_published: bool | None = None

    model_config = ConfigDict(extra="forbid")  # type: ignore[reportIncompatibleVariableOverride]
