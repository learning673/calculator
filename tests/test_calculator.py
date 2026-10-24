
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_addition():
    response = client.post(
        "/api/calculate",
        json={"a": 10, "b": 5, "operation": "add"},
    )
    assert response.status_code == 200
    assert response.json()["result"] == 15

def test_division():
    response = client.post(
        "/api/calculate",
        json={"a": 10, "b": 2, "operation": "divide"},
    )
    assert response.status_code == 200
    assert response.json()["result"] == 5

def test_division_by_zero():
    response = client.post(
        "/api/calculate",
        json={"a": 10, "b": 0, "operation": "divide"},
    )
    assert response.status_code == 400

def test_invalid_operation():
    response = client.post(
        "/api/calculate",
        json={"a": 10, "b": 5, "operation": "power"},
    )
    assert response.status_code == 422
