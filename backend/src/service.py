from typing import List, Dict

from .data import streams
from .stream import CreateStream, Stream


class StreamsService:
    def __init__(self):
        pass

    def get_all(self) -> Dict[str, Stream]:
        return streams

    def get_by_id(self, stream_id: str) -> Stream:
        return streams[stream_id]

    def create(self, stream: CreateStream) -> None:
        new_id = str(len(streams) + 1)
        new_stream = Stream(id=new_id, title=stream.title, description=stream.description)
        streams[new_id] = new_stream

    def update(self, stream_id: str, title: str, description: str) -> None:
        stream = Stream(id=stream_id, title=title, description=description)
        streams[stream_id] = stream

    def delete(self, stream_id: str) -> None | str:
        res = streams.pop(stream_id, "Id стрима не действителен")
        return res if isinstance(res, str) else f"Stream({res}) успешно удален"


streams_service = StreamsService()
