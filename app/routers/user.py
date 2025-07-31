from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def read_users():
    return {"message": "Good News, everynone!"}


@router.get("/{user_id}")
async def read_user(user_id: int):
    return {"message": user_id}
