# tests/test_users.py
from fastapi.testclient import TestClient
from app.main import app
from faker import Faker

fake = Faker()
fake_zh = Faker("zh_CN")


client = TestClient(app)

def test_create_user():
    # username = fake.name()
    username = fake_zh.name()
    response = client.post(
        "/users/register",
        json={"username": username, "email": fake.email(), "password": fake.password(length=7)}
    )
    assert response.status_code == 200
    assert response.json()["username"] == username