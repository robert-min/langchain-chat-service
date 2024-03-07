import os
from typing import ClassVar
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


# load env
load_dotenv()


class EnvSettings(BaseSettings):
    POSTGRESQL_CONNECTION_URL = os.environ.get(
        'POSTGRESQL_CONNECTION_URL'
    )
    POSTGRESQL_DB_NAME: ClassVar[str] = os.environ.get('POSTGRESQL_DB_NAME')
    MONGO_CONNECTION_URL: ClassVar[str] = os.environ.get(
        'MONGO_CONNECTION_URL'
    )
    MONGO_DB_NAME: ClassVar[str] = os.environ.get('MONGO_DB_NAME')


# set config
settings = EnvSettings()
