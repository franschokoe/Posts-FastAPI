from fastapi.testclient import TestClient
from app.main import app
from fastapi import status

client = TestClient(app)

def test_root():
    res = client.get("/")
    assert res.json().get("Posts") == "Social posts"
    assert res.status_code == 200



def test_create_user():
    response = client.post("/users" , json={"email" : "kai@gmail.com" , "password": "kai123"})
    print(response.json())
    assert response.status_code == status.HTTP_201_CREATED