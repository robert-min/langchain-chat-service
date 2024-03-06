import os
from typing import ClassVar
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


# load env
load_dotenv()


class EnvSettings(BaseSettings):
    MONGO_CONNECTION_URL: ClassVar[str] = os.environ.get(
        'MONGO_CONNECTION_URL'
    )
    MONGO_DB_NAME: ClassVar[str] = os.environ.get('MONGO_DB_NAME')


# set config
settings = EnvSettings()
