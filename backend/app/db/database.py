from typing import Dict, List, Any, Tuple

import psycopg2

from ..db import config
from ..stream import Stream, CreateStream


class StreamsService:
    def sql_request(self, request: str, params: List[Any] = None, need_return: bool = True) -> List[Tuple[Any]] | list:
        connection = psycopg2.connect(**config.DB_PARAMS)
        result = []

        with connection.cursor() as cursor:
            cursor.execute(request) if params is None else cursor.execute(request, params)
            if need_return:
                result = cursor.fetchall()

        connection.commit()
        connection.close()
        return result

    def get_all(self) -> Dict[str, Stream]:
        response = self.sql_request("""SELECT * FROM stream_service_data_test""")

        return {str(stream[0]): Stream(id=str(stream[0]), title=stream[1], description=stream[2]) for stream in
                response}

    def get_by_id(self, stream_id: str) -> Dict[str, Stream] | str:
        response = self.sql_request("""
                                    SELECT * FROM stream_service_data_test
                                    WHERE id = %s
                                            """,
                                    params=[stream_id]
                                    )
        if not response:
            return 'Id стрима не действителен'
        return {str(response[0][0]): Stream(id=str(response[0][0]), title=response[0][1], description=response[0][2])}

    def create(self, stream: CreateStream) -> str:
        self.sql_request("""
                         INSERT INTO stream_service_data_test (title, description)
                         VALUES (%s, %s);                           
                                """,
                         params=[stream.title, stream.description], need_return=False
                         )
        return "Стрим успешно создан"

    def update(self, stream_id: str, title: str, description: str) -> str:
        self.sql_request("""
                         UPDATE stream_service_data_test 
                         SET title = %s, description = %s
                         WHERE id = %s
                                """,
                         params=[title, description, stream_id], need_return=False
                         )
        return "Данные о стриме успешно обновлены"

    def delete(self, stream_id: str) -> str:
        self.sql_request("""
                                DELETE FROM stream_service_data_test 
                                WHERE id = %s
                                """,
                         params=[stream_id], need_return=False
                         )
        return "Стрим успешно удален"

    def drop(self) -> str:
        self.sql_request("""DELETE FROM stream_service_data_test""", need_return=False)
        return "Таблица успешно очищена"


streams_service_db = StreamsService()
