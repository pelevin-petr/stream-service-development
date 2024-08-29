from sqlalchemy import Integer, MetaData, String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

metadata_obj = MetaData()


class Base(DeclarativeBase):
    metadata = metadata_obj

    repr_cols_num = 3  # Надо будет увеличить, когда будет больше столбцов
    repr_cols = tuple()


class StreamsOrm(Base):
    __tablename__ = "stream_service_data_test_ORM"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]


class InstructorsOrm(Base):
    __tablename__ = "instructors_service_data_test_ORM"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    fullname: Mapped[str]
    work_experience: Mapped[str]


