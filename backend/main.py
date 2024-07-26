from fastapi import FastAPI, APIRouter

from src.service import streams_service
from src.stream import CreateStream, Stream
from src.db.database import streams_service_db


app = FastAPI(
    title="Stream Service",
)

router = APIRouter(prefix='/api')


@router.get("/streams")
def read_streams():
    return streams_service_db.get_all()


@router.get("/streams/{stream_id}")
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
    return streams_service_db.delete_all()


app.include_router(router)
