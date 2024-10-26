from typing import Optional

from fastapi import UploadFile
from pydantic import BaseModel, Field, ConfigDict


class BaseStream(BaseModel): 
    title: str = Field(min_length=1, max_length=50)
    description: str = Field(min_length=0, max_length=100)
    # file: bytes = Field(min_length=0)


class CreateStream(BaseStream):
    pass


class Stream(BaseStream):
    id: int

    model_config = ConfigDict(from_attributes=True)
