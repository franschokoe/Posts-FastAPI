from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    res = client.get("/")
    assert res.json().get("Posts") == "Social posts"
    assert res.status_code == 200



def test_create_user():
    response = client.post("/users" , json={"email" : "poo@gmail.com" , "password": "poo123"})
    print(response.json())
    assert response.status_code ==201