# # app/routes.py

# from flask import Blueprint, request, jsonify, render_template, redirect, url_for
# from app import storage

# # ✅ This is what the error says is missing
# bp = Blueprint('routes', __name__)

# @bp.route('/')
# def index():
#     tasks = storage.list_tasks()
#     return render_template('index.html', tasks=tasks)

# @bp.route('/tasks', methods=['POST'])
# def create_task():
#     if request.is_json:
#         data = request.get_json()
#         if not data or 'description' not in data:
#             return jsonify({'error': 'Missing description'}), 400
#         task = storage.add_task(data['description'])
#         return jsonify({'description': task.description, 'done': task.done}), 201
#     else:
#         desc = request.form.get('description')
#         if desc:
#             storage.add_task(desc)
#         return redirect(url_for('routes.index'))

# @bp.route('/tasks', methods=['GET'])
# def get_tasks():
#     tasks = storage.list_tasks()
#     return jsonify([{'description': t.description, 'done': t.done} for t in tasks])
# app/routes.py
from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from app import storage

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    tasks = storage.list_tasks()
    return render_template('index.html', tasks=tasks)

@bp.route('/tasks', methods=['POST'])
def create_task():
    # Handle JSON (API) or Form (browser)
    if request.is_json:
        data = request.get_json()
        if not data or 'description' not in data:
            return jsonify({'error': 'Missing description'}), 400
        task = storage.add_task(data['description'])
        return jsonify({'description': task.description, 'done': task.done}), 201
    else:
        desc = request.form.get('description')
        if desc:
            storage.add_task(desc)
        return redirect(url_for('routes.index'))

@bp.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = storage.list_tasks()
    return jsonify([{'description': t.description, 'done': t.done} for t in tasks])

@bp.route('/tasks/<int:task_id>/done', methods=['POST'])
def mark_done(task_id):
    storage.mark_done(task_id)
    return redirect(url_for('routes.index'))

@bp.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    storage.delete_task(task_id)
    return redirect(url_for('routes.index'))
