from typing import List, Dict

from fastapi import FastAPI, APIRouter, Request, status
from fastapi.encoders import jsonable_encoder
from pydantic import ValidationError
from fastapi.responses import JSONResponse

from src.db_orm.service import streams_service

app = FastAPI(
    title="Stream Service",
)

router = APIRouter(prefix='/api')


@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()})
    )


@router.get("/streams")
def read_streams() -> list[dict] | str:
    streams = streams_service.get_all()
    if not streams:
        return "Streams not found"
    return streams


@router.get("/streams/{stream_id}")
def read_stream(stream_id: str) -> str | dict:
    stream = streams_service.get_by_id(stream_id)
    if not stream:
        return "Stream not found"
    return stream


@router.post("/streams")
def create_stream(title: str, description: str):
    return streams_service.create(title, description)


@router.put("/streams")
def update_stream(stream_id: str, title: str, description: str) -> str | dict:
    stream = streams_service.update(stream_id, title, description)
    if stream is None:
        return 'Stream does not exist'
    return stream


@router.delete("/streams")
def delete_stream(stream_id: str) -> str | dict:
    stream = streams_service.delete(stream_id)
    if stream is None:
        return "Stream does not exist"
    return stream


app.include_router(router)
