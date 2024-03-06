import pymongo
from shared.infra.config import settings


def get_mongo_session():
    client = pymongo.MongoClient(
        settings.MONGO_CONNECTION_URL
    )
    return client[settings.MONGO_DB_NAME]
