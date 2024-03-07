import pytest
from shared.infra.database.connection import get_postgre_session


@pytest.fixture
def postgre_session():
    return get_postgre_session()
