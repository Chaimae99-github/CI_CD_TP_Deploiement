import requests


BASE_URL = "http://localhost:8080"


def test_health():
    response = requests.get(f"{BASE_URL}/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_addition():
    response = requests.get(f"{BASE_URL}/addition")

    assert response.status_code == 200
    assert response.json()["result"] == 5
