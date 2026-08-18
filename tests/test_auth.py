from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_valid_login():
    response = client.post(
        "/api/auth/login",
        params={
            "username": "alice",
            "password": "password123",
        },
    )

    assert response.status_code == 200
    assert response.json()["authenticated"] is True


def test_invalid_login():
    response = client.post(
        "/api/auth/login",
        params={
            "username": "alice",
            "password": "wrong",
        },
    )

    assert response.status_code == 401