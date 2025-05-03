from app.models import Task

tasks = []

def add_task(description):
    task = Task(description)
    tasks.append(task)
    return task

def list_tasks():
    return tasks

def clear_tasks():
    tasks.clear()

def mark_done(index):
    if 0 <= index < len(tasks):
        tasks[index].mark_done()

def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)