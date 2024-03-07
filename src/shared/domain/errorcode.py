from enum import Enum
from starlette import status


class RepositoryError(Enum):
    NotFoundData = {
        "code": status.HTTP_404_NOT_FOUND,
        "message": "The data isn't existence on DB. Please check data.",
        "log": "User Error. Request non data on DB."
    }
    DBProcess = {
        "code": status.HTTP_500_INTERNAL_SERVER_ERROR,
        "message": "Failed to connect. Contact service administrator.",
        "log": "DB Process Error. Check DB module."
    }
    DBNoNExist = {
        "code": status.HTTP_500_INTERNAL_SERVER_ERROR,
        "message": "Failed to connect. Contact service administrator.",
        "log": "DB Not created. Check DB infra."
    }
