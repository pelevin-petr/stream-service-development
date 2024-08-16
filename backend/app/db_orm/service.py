from copy import deepcopy

from sqlalchemy import select
from sqlalchemy.sql.operators import or_

from db_orm.database import engine, session_factory
from db_orm.models import Base, StreamsOrm
from stream import Stream, CreateStream


class StreamsService:
    @staticmethod
    def create_tables():
        Base.metadata.create_all(engine)

    @staticmethod
    def get_all(filter_params: str | None) -> list:
        with session_factory() as session:
            query = select(StreamsOrm)

            if filter_params is not None:
                if filter_params.isdigit():
                    query = query.where(StreamsOrm.id == int(filter_params))
                else:
                    query = query.where(
                        or_(
                            StreamsOrm.title.like(f"%{filter_params}%"),
                            StreamsOrm.description.like(f"%{filter_params}%")
                        )
                    )

            result = session.execute(query)
            res = result.scalars().all()
            return res

    @staticmethod
    def get_by_id(stream_id: int) -> Stream | None:
        with session_factory() as session:
            query = (
                select(StreamsOrm)
                .where(StreamsOrm.id == stream_id)
            )
            result = session.execute(query)
            stream = result.all()

            if not stream:
                return
            return stream[0][0]

    @staticmethod
    def create(stream: CreateStream) -> Stream:
        with session_factory() as session:
            new_stream = StreamsOrm(title=stream.title, description=stream.description)
            session.add(new_stream)
            session.commit()
            return Stream(id=new_stream.id, title=new_stream.title, description=new_stream.description)

    @staticmethod
    def update(stream_id: int, new_stream: CreateStream) -> Stream | None:
        with session_factory() as session:
            stream = session.get(StreamsOrm, stream_id)

            if stream is None:
                return

            stream.title = new_stream.title
            stream.description = new_stream.description
            response = deepcopy(stream)
            session.commit()

            return response

    @staticmethod
    def delete(stream_id: int) -> Stream | None:
        with session_factory() as session:
            stream = session.get(StreamsOrm, stream_id)

            if stream is None:
                return

            session.delete(stream)
            session.commit()

            return stream


streams_service = StreamsService()
