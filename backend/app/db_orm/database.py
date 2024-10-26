from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_orm.config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME


DATABASE_URL_psycopg = f"postgresql+psycopg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


engine = create_engine(
    url=DATABASE_URL_psycopg,
    echo=False,
)

session_factory = sessionmaker(engine)
