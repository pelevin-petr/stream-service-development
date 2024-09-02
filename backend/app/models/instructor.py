from pydantic import BaseModel, Field, ConfigDict


class BaseInstructor(BaseModel):
    fullname: str = Field(min_length=1, max_length=50)
    work_experience: str = Field(min_length=0, max_length=100)


class CreateInstructor(BaseInstructor):
    pass


class Instructor(BaseInstructor):
    id: int

    model_config = ConfigDict(from_attributes=True)
