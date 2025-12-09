from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_get_user_returns_username_and_email():
    response = client.get("/user")

    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "john_doe"
    assert data["email"] == "john@example.com"
