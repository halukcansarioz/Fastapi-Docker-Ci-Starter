import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_get_item():
    payload = {"name": "Widget", "description": "A useful widget", "price": 19.99}
    create_response = client.post("/items", json=payload)
    assert create_response.status_code == 201
    created = create_response.json()
    assert created["name"] == "Widget"
    assert created["description"] == "A useful widget"
    assert created["price"] == 19.99
    item_id = created["id"]

    get_response = client.get(f"/items/{item_id}")
    assert get_response.status_code == 200
    assert get_response.json() == created


def test_get_item_not_found():
    response = client.get("/items/999999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"
