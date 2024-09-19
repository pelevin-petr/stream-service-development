from typing import Optional, Tuple, List, Any, Dict

from fastapi import FastAPI, APIRouter, Request, status, HTTPException, Form, UploadFile, File
from fastapi.encoders import jsonable_encoder
from pydantic import ValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from db_orm.instructor_service import instructors_service
from db_orm.stream_service import streams_service
from models.instructor import Instructor, CreateInstructor
from models.stream import Stream, CreateStream

app = FastAPI(
    title="Stream Service",
)

router = APIRouter(prefix='/api')

streams_service.create_tables()
instructors_service.create_tables()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174", "http://localhost:5173", "http://localhost:4173"],
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


@router.get("/streams", response_model=List[Dict[str, Any]])
def read_streams(filter_params: str | None = None) -> List[Dict[str, Any]]:
    streams = streams_service.get_all(filter_params)
    if not streams:
        raise HTTPException(status_code=404, detail="Streams not found")
    return streams


@router.get("/streams/{stream_id}", response_model=Dict[str, Any])
def read_stream(stream_id: int) -> Dict[str, Any]:
    stream = streams_service.get_by_id(stream_id)
    if not stream:
        raise HTTPException(status_code=404, detail="Stream not found")
    return stream


@router.post("/streams", response_model=Dict[str, Any])
def create_stream(
        title: str = Form(...),
        description: str = Form(None),
        file: Optional[UploadFile] = File()
) -> Dict[str, Any]:
    return streams_service.create(title, description, file)


@router.put("/streams", response_model=Dict[str, Any])
def update_stream(
        stream_id: int,
        title: str = Form(...),
        description: str = Form(None),
        file: Optional[UploadFile] = File()
) -> Dict[str, Any]:
    stream = streams_service.update(stream_id, title, description, file)

    if stream is None:
        raise HTTPException(status_code=404, detail="Stream not found")
    return stream


@router.delete("/streams", response_model=Dict[str, Any])
def delete_stream(stream_id: int) -> Dict[str, Any]:
    stream = streams_service.delete(stream_id)
    if stream is None:
        raise HTTPException(status_code=404, detail="Stream not found")
    return stream


@router.get("/instructors", response_model=list[Instructor])
def read_instructors(filter_params: str | None = None):
    instructors = instructors_service.get_all(filter_params)
    if not instructors:
        raise HTTPException(status_code=404, detail="Instructors not found")
    return instructors


@router.get("/instructors/{instructors_id}", response_model=Instructor)
def read_instructor(instructor_id: int) -> Instructor:
    instructor = instructors_service.get_by_id(instructor_id)
    if not instructor:
        raise HTTPException(status_code=404, detail="Instructor not found")
    return instructor


@router.post("/instructors", response_model=Instructor)
def create_instructor(instructor: CreateInstructor) -> Instructor:
    return instructors_service.create(instructor)


@router.put("/instructors", response_model=Instructor)
def update_instructor(instructor_id: int, instructor: CreateInstructor) -> Instructor:
    instructor = instructors_service.update(instructor_id, instructor)
    if instructor is None:
        raise HTTPException(status_code=404, detail="Instructor not found")
    return instructor


@router.delete("/instructors", response_model=Instructor)
def delete_instructor(instructor_id: int) -> Instructor:
    instructor = instructors_service.delete(instructor_id)
    if instructor is None:
        raise HTTPException(status_code=404, detail="Instructor not found")
    return instructor


app.include_router(router)
