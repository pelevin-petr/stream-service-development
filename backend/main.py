from fastapi import FastAPI, APIRouter

from service import streams_service
from stream import CreateStream

app = FastAPI()

router = APIRouter(prefix='/api')


@router.get("/streams")
def read_streams():
    return streams_service.get_all()


@router.get("/streams/{stream_id}")
def read_stream(stream_id: str):
    return streams_service.get_by_id(stream_id)


@router.post("/streams")
def create_stream(stream: CreateStream):
    return streams_service.create(stream)


app.include_router(router)
