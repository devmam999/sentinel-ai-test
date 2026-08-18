from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_get_existing_user():
    response = client.get("/api/users/1")

    assert response.status_code == 200
    assert response.json()["username"] == "alice"


def test_get_missing_user():
    response = client.get("/api/users/999")

    assert response.status_code == 404