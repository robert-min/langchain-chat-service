import pytest
from fastapi.testclient import TestClient
from shared.infra.database.connection import get_postgre_session
from shared.presentation.rest.api import create_app


@pytest.fixture
def postgre_session():
    return get_postgre_session()


@pytest.fixture
def client():
    app = create_app()
    yield TestClient(app)
