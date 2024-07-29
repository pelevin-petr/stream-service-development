from sqlalchemy import select

from backend.src.db_orm.database import engine, session_factory
from backend.src.db_orm.models import Base, StreamsOrm


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
            print(f"{res}")

    @staticmethod
    def get_by_id(stream_id: str):
        with session_factory() as session:
            query = (
                select(StreamsOrm)
                .where(StreamsOrm.id == stream_id)
            )
            session.execute(query)
            return session.fetchall()

    @staticmethod
    def create_stream():
        with session_factory() as session:
            worker_jack = StreamsOrm(title="ORM", description="ORM descr")
            session.add_all([worker_jack])
            session.commit()


stream_service = StreamsService()
stream_service.create_tables()
stream_service.get_all()
