from fastapi import APIRouter, HTTPException, status
from sqlmodel import select

from app.db.session import DB_SESSION
from app.models.user import User

router = APIRouter()


@router.get("/")
async def read_users(session: DB_SESSION):
    result = await session.execute(select(User))
    users = result.scalars().all()
    return users


@router.get("/{user_id}")
async def read_user(user_id: int, session: DB_SESSION):
    user = await session.get(User, user_id)

    if user:
        return {"user": user.name}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=("User not found."),
    )


@router.post("/")
async def create_user(user: User, session: DB_SESSION):
    db_user = User.model_validate(user)
    session.add(db_user)
    await session.commit()
    return db_user


@router.patch("/{user_id}")
async def update_user(user_id: int, session: DB_SESSION, user: User):
    db_user = await session.get(User, user_id)

    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=("User not found."),
        )

    user_data = user.model_dump(exclude_unset=True)
    db_user.sqlmodel_update(user_data)
    session.add(db_user)
    await session.commit()

    return db_user


@router.delete("/{user_id}")
async def delete_user(user_id: int, session: DB_SESSION):
    db_user = await session.get(User, user_id)

    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=("User not found."),
        )
    user_name = db_user.name
    await session.delete(db_user)
    await session.commit()

    return {"message": f"User: {user_name.capitalize()} deleted!"}
