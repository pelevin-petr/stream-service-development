import base64
from copy import deepcopy
from typing import List, Dict, Any

from fastapi import UploadFile
from sqlalchemy import select, cast, String
from sqlalchemy.sql.operators import or_

from db_orm.database import engine, session_factory
from db_orm.ORM_models import Base, StreamsOrm
import minio_service.service as minio_service
from models.stream import Stream, CreateStream

bucket_name = 'bucket-streams'


class StreamsService:
    @staticmethod
    def create_tables():
        Base.metadata.create_all(engine)

    @staticmethod
    def get_all(filter_params: str | None) -> List[Dict[str, str | None | Any]]:
        with session_factory() as session:
            query = select(StreamsOrm)

            if filter_params is not None:
                if filter_params.isdigit():
                    query = query.where(cast(StreamsOrm.id, String).like(f"%{filter_params}%"))
                else:
                    query = query.where(
                        or_(
                            StreamsOrm.title.like(f"%{filter_params}%"),
                            StreamsOrm.description.like(f"%{filter_params}%")
                        )
                    )

            result = session.execute(query)
            res = result.scalars().all()

            response = []
            for stream in res:
                stream_data = {
                    'id': stream.id,
                    'title': stream.title,
                    'description': stream.description,
                }
                response.append(
                    {"stream": stream_data, 'file_url': minio_service.get_files_url(bucket_name, str(stream.id))})
            return response

    @staticmethod
    def get_by_id(stream_id: int) -> Dict[str, Any] | None:
        with session_factory() as session:
            query = (
                select(StreamsOrm)
                .where(StreamsOrm.id == stream_id)
            )
            result = session.execute(query)
            stream = result.all()

            if not stream:
                return

            file = minio_service.get_files_url(bucket_name, str(stream[0][0].id))
            stream_data = {
                'id': stream[0][0].id,
                'title': stream[0][0].title,
                'description': stream[0][0].description,
            }
            return {'Stream': stream_data, 'file_url': file}

    @staticmethod
    def create(title, description, file) -> Dict[str, Any]:
        if description is None:
            description = ''

        with session_factory() as session:
            new_stream = StreamsOrm(title=title, description=description)
            session.add(new_stream)
            session.commit()

            minio_service.upload_file(file, bucket_name, str(new_stream.id))
            file = minio_service.get_files_url(bucket_name, str(new_stream.id))

            stream_data = {
                'id': new_stream.id,
                'title': new_stream.title,
                'description': new_stream.description,
            }
            return {'Stream': stream_data, 'file_url': file}

    @staticmethod
    def update(stream_id: int, title: str, description: str, file: UploadFile) -> Dict[str, Any] | None:
        with session_factory() as session:
            stream = session.get(StreamsOrm, stream_id)

            if stream is None:
                return

            stream.title = title
            stream.description = description
            response = deepcopy(stream)
            session.commit()

            minio_service.upload_file(file, bucket_name, str(stream_id))
            file = minio_service.get_files_url(bucket_name, str(stream_id))

            stream_data = {
                'id': response.id,
                'title': response.title,
                'description': response.description,
            }
            return {'Stream': stream_data, 'file_url': file}

    @staticmethod
    def delete(stream_id: int) -> Dict[str, Any] | None:
        with session_factory() as session:
            stream = session.get(StreamsOrm, stream_id)

            if stream is None:
                return

            stream_data = {
                'id': stream.id,
                'title': stream.title,
                'description': stream.description,
            }

            session.delete(stream)
            session.commit()

            return {'Stream': stream_data, 'file_url': 'Image was deleted'}


streams_service = StreamsService()
