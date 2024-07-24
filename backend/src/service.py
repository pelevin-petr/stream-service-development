from data import streams
from stream import CreateStream, Stream


class StreamsService:
    def __init__(self):
        pass

    def get_all(self):
        return streams

    def get_by_id(self, stream_id):
        return streams[stream_id]

    def create(self, stream: CreateStream):
        new_id = str(len(streams) + 1)
        new_stream = Stream(id=new_id, title=stream.title, description=stream.description)
        streams[new_id] = new_stream


streams_service = StreamsService()
