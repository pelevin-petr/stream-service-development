import psycopg2
import config

connection = psycopg2.connect(**config.DB_PARAMS)

with connection.cursor() as cursor:
    cursor.execute("""
        SELECT title FROM stream_service_data_test
        WHERE id = 2;   
                    """)
    print(cursor.fetchall())


connection.close()
