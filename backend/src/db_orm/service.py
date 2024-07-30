from sqlalchemy import select

from src.db_orm.database import engine, session_factory
from src.db_orm.models import Base, StreamsOrm


class StreamsService:
    @staticmethod
    def create_tables():
        Base.metadata.create_all(engine)

    @staticmethod
    def get_all() -> list:
        with session_factory() as session:
            query = select(StreamsOrm)
            result = session.execute(query)
            res = result.scalars().all()
            streams = []

            for row in res:
                stream = {
                    'id': row.id,
                    'title': row.title,
                    'description': row.description,
                }
                streams.append(stream)

            return streams

    @staticmethod
    def get_by_id(stream_id: str) -> dict | None:
        with session_factory() as session:
            query = (
                select(StreamsOrm)
                .where(StreamsOrm.id == int(stream_id))
            )
            result = session.execute(query)
            stream = result.all()

            if not stream:
                return
            return {
                'id': str(stream[0][0].id),
                'title': stream[0][0].title,
                'description': stream[0][0].description,
            }

    @staticmethod
    def create(title: str, description: str) -> dict:
        with session_factory() as session:
            stream = StreamsOrm(title=title, description=description)
            session.add(stream)
            session.commit()

            return {
                'id': stream.id,
                'title': stream.title,
                'description': stream.description,
            }

    @staticmethod
    def update(stream_id: str, new_title: str, new_description: str) -> dict | None:
        with session_factory() as session:
            stream = session.get(StreamsOrm, stream_id)

            if stream is None:
                return

            stream.title = new_title
            stream.description = new_description
            session.commit()

            return {
                'id': stream.id,
                'title': stream.title,
                'description': stream.description,
            }

    @staticmethod
    def delete(stream_id: str) -> dict | None:
        with session_factory() as session:
            stream = session.get(StreamsOrm, stream_id)

            if stream is None:
                return

            session.delete(stream)
            session.commit()

            return {
                'id': stream.id,
                'title': stream.title,
                'description': stream.description,
            }


streams_service = StreamsService()
