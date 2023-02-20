from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.scoping import ScopedSession
from sqlalchemy.engine.base import Engine
from typing import Any, Generator
import os

DB_USER = os.environ.get('MYSQL_USER')
DB_PASSWORD = os.environ.get('MYSQL_PASSWORD')
DB_HOST = os.environ.get('MYSQL_HOST')
DB_PORT = os.environ.get('MYSQL_PORT')
DB_NAME = os.environ.get('MYSQL_DATABASE')


DATABASE: str = "mysql://%s:%s@%s/%s?charset=utf8mb4" % (
    DB_USER,
    DB_PASSWORD,
    f'{DB_HOST}:{DB_PORT}',
    DB_NAME,
)
print('DATABASE' , DATABASE)
engine: Engine = create_engine(
    DATABASE,
    # encoding='utf-8',
    echo=True
)
SessionLocal: ScopedSession = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base: Any = declarative_base()
Base.query = SessionLocal.query_property()


def get_db() -> Generator[Session, None, None]:
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()