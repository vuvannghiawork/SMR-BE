import settings
import os
from database.models import Base
import sqlalchemy
from urllib.parse import quote
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


def connect_tcp_socket():
    pool = create_engine(
        sqlalchemy.engine.url.URL.create(
            drivername="postgresql+psycopg2",
            username=settings.POSTGRES_USER,
            password=settings.POSTGRES_PASSWORD,
            host=settings.POSTGRES_HOST,
            port=settings.POSTGRES_PORT,
            database=settings.POSTGRES_DB,
        ),
        echo=settings.FASTAPI_ENVIRONMENT == "DEVELOPMENT",
        pool_pre_ping=True,
        # ...
    )
    return pool


engine_pool = connect_tcp_socket()
Base.metadata.create_all(engine_pool)
Session = sessionmaker(bind=engine_pool)
