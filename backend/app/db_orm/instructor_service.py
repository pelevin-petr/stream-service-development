from copy import deepcopy

from sqlalchemy import select, cast, String
from sqlalchemy.sql.operators import or_

from db_orm.database import engine, session_factory
from db_orm.ORM_models import Base, InstructorsOrm
from models.instructor import CreateInstructor, Instructor


class InstructorsService:
    @staticmethod
    def create_tables():
        Base.metadata.create_all(engine)

    @staticmethod
    def get_all(filter_params: str | None) -> list:
        with session_factory() as session:
            query = select(InstructorsOrm)

            if filter_params is not None:
                if filter_params.isdigit():
                    query = query.where(cast(InstructorsOrm.id, String).like(f"%{filter_params}%"))
                else:
                    query = query.where(
                        or_(
                            InstructorsOrm.fullname.like(f"%{filter_params}%"),
                            InstructorsOrm.work_experience.like(f"%{filter_params}%")
                        )
                    )

            result = session.execute(query)
            res = result.scalars().all()
            return res

    @staticmethod
    def get_by_id(instructor_id: int) -> Instructor | None:
        with session_factory() as session:
            query = (
                select(InstructorsOrm)
                .where(InstructorsOrm.id == instructor_id)
            )
            result = session.execute(query)
            stream = result.all()

            if not stream:
                return
            return stream[0][0]

    @staticmethod
    def create(instructor: CreateInstructor) -> Instructor:
        with session_factory() as session:
            new_instructor = InstructorsOrm(fullname=instructor.fullname, work_experience=instructor.work_experience)
            session.add(new_instructor)
            session.commit()
            return Instructor(id=new_instructor.id, fullname=new_instructor.fullname, work_experience=new_instructor.work_experience)

    @staticmethod
    def update(instructor_id: int, new_instructor: CreateInstructor) -> Instructor | None:
        with session_factory() as session:
            instructor = session.get(InstructorsOrm, instructor_id)

            if instructor is None:
                return

            instructor.fullname = new_instructor.fullname
            instructor.work_experience = new_instructor.work_experience
            response = deepcopy(instructor)
            session.commit()

            return response

    @staticmethod
    def delete(instructor_id: int) -> Instructor | None:
        with session_factory() as session:
            instructor = session.get(InstructorsOrm, instructor_id)

            if instructor is None:
                return

            session.delete(instructor)
            session.commit()

            return instructor


instructors_service = InstructorsService()
instructors_service.create_tables()
