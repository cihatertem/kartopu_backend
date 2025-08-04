from typing import Annotated
from uuid import UUID
from fastapi.params import Depends
from sqlmodel import select
from app.crud.base import BaseService
from app.db.session import db_session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


class UserService(BaseService):
    async def get_all(self, limit: int = 0, offset: int = 0) -> list[User]:
        result = await self.session.execute(select(User).limit(limit).offset(offset))
        users = result.scalars().all()
        return list(users)

    async def get_one(self, user_id: UUID) -> User:
        user = await self.session.get_one(User, user_id)
        return user

    async def create(self, user_data: UserCreate) -> User:
        db_user = User.model_validate(user_data)
        self.session.add(db_user)
        await self.session.commit()
        return db_user

    async def update(self, user_id: UUID, user_data: UserUpdate):
        db_user = await self.session.get_one(User, user_id)

        user_data_dump = user_data.model_dump(exclude_unset=True)

        db_user.sqlmodel_update(user_data_dump)
        self.session.add(db_user)
        await self.session.commit()

        return db_user

    async def delete(self, user_id: UUID) -> dict[str, str]:
        db_user = await self.session.get_one(User, user_id)

        user_name = db_user.username
        await self.session.delete(db_user)
        await self.session.commit()

        return {"message": f"User: {user_name.capitalize()} deleted!"}


def get_user_service(session: db_session) -> UserService:
    return UserService(session)


user_service = Annotated[UserService, Depends(get_user_service)]
