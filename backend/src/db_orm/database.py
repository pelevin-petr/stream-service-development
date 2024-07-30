from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_HOST = "localhost"
DB_PORT = "5432"
DB_USER = "postgres"
DB_PASS = "1111pelevin"
DB_NAME = "stream_service_db"

DATABASE_URL_psycopg = f"postgresql+psycopg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(
    url=DATABASE_URL_psycopg,
    echo=False,
)

session_factory = sessionmaker(engine)
