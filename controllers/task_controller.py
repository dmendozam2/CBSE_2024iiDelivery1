from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from services.task_service import TaskService
from models.task import Task

task_blueprint = Blueprint('tasks', __name__)

@task_blueprint.route('/tasks', methods=['POST'])
def create_task():

    data = request.form
    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    TaskService.create_task(name, description)
    return redirect(url_for('tasks.index'))

@task_blueprint.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = TaskService.get_tasks()
    tasks_dict = [task.to_dict() for task in tasks]
    return jsonify(tasks_dict)

@task_blueprint.route('/')
def index():
    return render_template('index.html')