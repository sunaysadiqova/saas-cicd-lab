import pytest
from app import app, tasks


@pytest.fixture
def client():
    app.config["TESTING"] = True
    tasks.clear()
    with app.test_client() as client:
        yield client


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_add_task(client):
    response = client.post("/api/tasks", json={"title": "CI/CD lab"})
    assert response.status_code == 201
    assert response.get_json()["title"] == "CI/CD lab"


def test_add_task_without_title(client):
    response = client.post("/api/tasks", json={})
    assert response.status_code == 400


def test_get_tasks(client):
    client.post("/api/tasks", json={"title": "task 1"})
    response = client.get("/api/tasks")
    assert response.status_code == 200
    assert len(response.get_json()) == 1
