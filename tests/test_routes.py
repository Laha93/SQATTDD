import pytest
from app.main import app
from app import storage  # Import this to access clear_tasks
import json

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_task_route(client):
    storage.clear_tasks()
    response = client.post('/tasks', json={'description': 'Buy eggplant'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['description'] == 'Buy eggplant'
    assert data['done'] is False

def test_get_tasks_route(client):
    storage.clear_tasks()
    client.post('/tasks', json={'description': 'Check fridge'})
    response = client.get('/tasks')
    assert response.status_code == 200
    tasks = response.get_json()
    assert any(t['description'] == 'Check fridge' for t in tasks)

def test_mark_task_done_route(client):
    storage.clear_tasks()
    client.post('/tasks', json={'description': 'Finish homework'})
    response = client.post('/tasks/0/done')
    assert response.status_code == 302
    tasks_response = client.get('/tasks')
    tasks = tasks_response.get_json()
    assert tasks[0]['done'] is True

def test_delete_task_route(client):
    storage.clear_tasks()
    client.post('/tasks', json={'description': 'Delete me'})
    tasks_response = client.get('/tasks')
    assert len(tasks_response.get_json()) == 1
    response = client.post('/tasks/0/delete')
    assert response.status_code == 302
    tasks_response = client.get('/tasks')
    assert len(tasks_response.get_json()) == 0
