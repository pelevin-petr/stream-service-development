from fastapi import FastAPI, APIRouter, Request, status, HTTPException, Header
from fastapi.encoders import jsonable_encoder
from pydantic import ValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from db_orm.service import streams_service
from stream import Stream, CreateStream

app = FastAPI(
    title="Stream Service",
)

router = APIRouter(prefix='/api')

streams_service.create_tables()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()})
    )


@router.get("/streams", response_model=list[Stream])
def read_streams(filter_params: str | None = None):
    streams = streams_service.get_all(filter_params)
    if not streams:
        raise HTTPException(status_code=404, detail="Streams not found")
    return streams


@router.get("/streams/{stream_id}", response_model=Stream)
def read_stream(stream_id: int) -> Stream:
    stream = streams_service.get_by_id(stream_id)
    if not stream:
        raise HTTPException(status_code=404, detail="Stream not found")
    return stream


@router.post("/streams", response_model=Stream)
def create_stream(stream: CreateStream) -> Stream:
    return streams_service.create(stream)


@router.put("/streams", response_model=Stream)
def update_stream(stream_id: int, stream: CreateStream) -> Stream:
    stream = streams_service.update(stream_id, stream)
    if stream is None:
        raise HTTPException(status_code=404, detail="Stream not found")
    return stream


@router.delete("/streams", response_model=Stream)
def delete_stream(stream_id: int) -> Stream:
    stream = streams_service.delete(stream_id)
    if stream is None:
        raise HTTPException(status_code=404, detail="Stream not found")
    return stream


app.include_router(router)
