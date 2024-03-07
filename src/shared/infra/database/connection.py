import pymongo
from shared.infra.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def get_mongo_session():
    client = pymongo.MongoClient(
        settings.MONGO_CONNECTION_URL
    )
    return client[settings.MONGO_DB_NAME]


def get_postgre_session() -> Session:
    engine = create_engine(
        settings.POSTGRESQL_CONNECTION_URL + settings.POSTGRESQL_DB_NAME,
        pool_size=5,
        pool_recycle=100,
        max_overflow=10
    )
    return Session(engine)
