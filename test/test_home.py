import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config.update(TESTING=True)
    with app.test_client() as client:
        yield client

def test_index_returns_hello(client):
    res = client.get("/")
    assert res.status_code == 200
    assert b"Hello, World!" in res.data
