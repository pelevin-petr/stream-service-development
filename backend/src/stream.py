from pydantic import BaseModel, Field


class BaseStream(BaseModel):
    title: str = Field(min_length=1, max_length=25)
    description: str = Field(min_length=1, max_length=100)


class CreateStream(BaseStream):
    pass


class Stream(BaseStream):
    id: str
