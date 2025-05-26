# tests/test_categories.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_admin_create_category():
    # 管理员登录获取token
    auth_response = client.post("/auth/login", json={
        "username": "admin",
        "password": "adminpass"
    })
    token = auth_response.json()["access_token"]
    
    # 创建分类
    response = client.post(
        "/categories/",
        json={"name": "Technology", "description": "Tech related articles"},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 201
    assert response.json()["name"] == "Technology"

def test_unauthorized_create_category():
    response = client.post(
        "/categories/",
        json={"name": "Test", "description": "Test category"}
    )
    assert response.status_code == 401