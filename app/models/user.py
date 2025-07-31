from sqlmodel import Field, SQLModel
# from app.db.session import SQLModel


class User(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    name: str = Field(index=True)
