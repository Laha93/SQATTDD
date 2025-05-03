from app import storage

def test_add_and_list_tasks():
    storage.clear_tasks()
    storage.add_task("Integration test task")
    result = storage.list_tasks()
    assert len(result) == 1
    assert result[0].description == "Integration test task"

def test_mark_task_done():
    storage.clear_tasks()
    storage.add_task("Mark me done")
    storage.mark_done(0)  # This function does NOT exist yet
    result = storage.list_tasks()
    assert result[0].done is True
    storage.clear_tasks()
    storage.add_task("Mark me done")
    storage.mark_done(0)  # This function doesn't exist yet — will fail
    result = storage.list_tasks()
    assert result[0].done is True
def test_delete_task():
    storage.clear_tasks()
    storage.add_task("Task to delete")
    assert len(storage.list_tasks()) == 1

    storage.delete_task(0)  # 🚨 This doesn't exist yet — expected to fail

    assert len(storage.list_tasks()) == 0
