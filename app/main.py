from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError, NoResultFound

from app.helpers.exceptions import NotFoundException
from app.routers import user


app = FastAPI(
    description="https://kartopu.money is a financial blog about FIRE. \
    And this fastapi application is backend API of the blog!",
    summary="Yet another blog backend API!",
    version="0.0.1",
)


@app.exception_handler(NotFoundException)
async def not_found_exception(req: Request, exc: NotFoundException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": f"{exc.not_found_name.capitalize()} not found!"},
    )


@app.exception_handler(IntegrityError)
async def database_integrity_error(req: Request, exc: IntegrityError):
    msg = str(exc.orig).split("DETAIL:")[-1].strip()
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"message": msg},
    )


@app.exception_handler(NoResultFound)
async def no_result_found(req: Request, exc: NoResultFound):
    msg = exc._message.__str__().split("('")[1].strip("')>\"")
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": msg},
    )


app.include_router(
    user.router,
    prefix="/users",
    tags=["users"],
)
