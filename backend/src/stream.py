from pydantic import BaseModel


class BaseStream(BaseModel):
    title: str
    description: str


class CreateStream(BaseStream):
    pass


class Stream(BaseStream):
    id: str
