# Test site home page returns a 200 response
from app import app


def test_home_page():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
