# tests/test_functional.py
from app.main import app
from app import storage

def test_task_lifecycle_functional():
    # Use Flask's test client to simulate browser interaction
    client = app.test_client()
    storage.clear_tasks()

    # 1. Create a task (simulate form submission)
    response = client.post('/tasks', data={'description': 'Functional Test Task'})
    assert response.status_code == 302  # Redirect to index

    # 2. Check task appears on homepage
    homepage = client.get('/')
    assert b'Functional Test Task' in homepage.data

    # 3. Mark it done
    client.post('/tasks/0/done')
    homepage = client.get('/')
    assert b'(Done)' in homepage.data

    # 4. Delete it
    client.post('/tasks/0/delete')
    homepage = client.get('/')
    assert b'Functional Test Task' not in homepage.data
