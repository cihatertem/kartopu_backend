from fastapi import FastAPI

from app.db.session import create_tables
from app.routers import user


app = FastAPI(
    description="https://kartopu.money is a financial blog about FIRE. \
    And this fastapi application is backend API of the blog!",
    summary="Yet another blog backend API.",
    version="0.0.1",
)


@app.on_event("startup")
async def on_startup():
    await create_tables()


app.include_router(
    user.router,
    prefix="/users",
    tags=["users"],
)
