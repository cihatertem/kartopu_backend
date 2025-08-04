from uuid import UUID
from fastapi import APIRouter
from app.crud.user import user_service
from app.models.user import User
from app.schemas.user import UserCreate, UserReponseBase, UserUpdate

router = APIRouter()


@router.get("/", response_model=list[UserReponseBase])
async def read_users(
    service: user_service, limit: int = 15, offset: int = 0
) -> list[User]:
    # TODO only admin
    result = await service.get_all(limit=limit, offset=offset)
    return result


@router.get("/{user_id}", response_model=UserReponseBase)
async def read_user(user_id: UUID, service: user_service):
    # TODO only admin & user owner
    user = await service.get_one(user_id)
    return user


@router.post("/", response_model=UserReponseBase)
async def create_user(user_data: UserCreate, service: user_service) -> User:
    new_user = await service.create(user_data)
    return new_user


@router.patch("/{user_id}", response_model_exclude_unset=True)
async def update_user(
    user_id: UUID, service: user_service, user_data: UserUpdate
) -> User:
    updated_user = await service.update(user_id, user_data)
    return updated_user


@router.delete("/{user_id}")
async def delete_user(user_id: UUID, service: user_service) -> dict[str, str]:
    return await service.delete(user_id)
