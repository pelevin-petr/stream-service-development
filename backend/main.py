from typing import List, Dict

from fastapi import FastAPI, APIRouter, Request, status
from fastapi.encoders import jsonable_encoder
from pydantic import ValidationError
from fastapi.responses import JSONResponse

from src.service import streams_service
from src.stream import CreateStream, Stream
from src.db.database import streams_service_db

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


@router.get("/streams", response_model=Dict[str, Stream])
def read_streams():
    return streams_service_db.get_all()


@router.get("/streams/{stream_id}", response_model=Dict[str, Stream])
def read_stream(stream_id: str):
    return streams_service_db.get_by_id(stream_id)


@router.post("/streams")
def create_stream(stream: CreateStream):
    return streams_service_db.create(stream)


@router.put("/streams")
def update_stream(stream_id: str, title: str, description: str):
    return streams_service_db.update(stream_id, title, description)


@router.delete("/streams")
def delete_stream(stream_id: str):
    return streams_service_db.delete(stream_id)


@router.delete("/streams/delete_streams")
def delete_streams():
    return streams_service_db.drop()


app.include_router(router)
