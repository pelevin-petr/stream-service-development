from sqlalchemy import select

from src.db_orm.database import engine, session_factory
from src.db_orm.models import Base, StreamsOrm
from src.stream import CreateStream


class StreamsService:
    @staticmethod
    def create_tables():
        Base.metadata.create_all(engine)

    @staticmethod
    def get_all():
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
    def get_by_id(stream_id: str):
        with session_factory() as session:
            query = select(StreamsOrm, stream_id)
            result = session.execute(query)
            stream = result.one_or_none()

            if stream is None:
                return

            return {
                'id': stream.id,
                'title': stream.title,
                'description': stream.description,
            }

    @staticmethod
    def create(stream: CreateStream = CreateStream(title='123', description='123')):
        with session_factory() as session:
            stream = StreamsOrm(title=stream.title, description=stream.description)
            session.add(stream)
            session.commit()
            print({
                'id': stream.id,
                'title': stream.title,
                'description': stream.description,
            })
            return {
                'id': stream.id,
                'title': stream.title,
                'description': stream.description,
            }

    @staticmethod
    def update(stream_id: str, new_title: str, new_description: str):
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
    def delete(stream_id: str):
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
print(streams_service.create_tables())
