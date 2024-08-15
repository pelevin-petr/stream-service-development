from sqlalchemy import Integer, MetaData
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass

    repr_cols_num = 3  # Надо будет увеличить, когда будет больше столбцов
    repr_cols = tuple()


class StreamsOrm(Base):
    __tablename__ = "stream_service_data_test_ORM"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]


metadata_obj = MetaData()
