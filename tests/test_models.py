from app.models import Task

def test_task_creation():
    task = Task("Buy milk")
    assert task.description == "Buy milk"
    assert task.done is False
def test_task_can_be_marked_done():
    task = Task("Complete homework")
    task.mark_done()
    assert task.done is True