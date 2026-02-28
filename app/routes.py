
from flask import render_template
from flask import Blueprint, request, jsonify, session
from app import db
from app.models import Task
from app.utils import login_required

task_bp = Blueprint("tasks", __name__)

@task_bp.route("/tasks", methods=["POST"])
@login_required
def create_task():
    data = request.get_json()
    title = data.get("title")

    if not title:
        return jsonify({"error": "Title required"}), 400

    task = Task(
        title=title,
        user_id=session["user_id"]
    )

    db.session.add(task)
    db.session.commit()

    return jsonify({"message": "Task created"}), 201


@task_bp.route("/tasks", methods=["GET"])
@login_required
def get_tasks():
    tasks = Task.query.filter_by(user_id=session["user_id"]).all()

    return jsonify([
        {
            "id": task.id,
            "title": task.title,
            "status": task.status
        } for task in tasks
    ])
@task_bp.route("/")
def home_page():
    return render_template("index.html")

@task_bp.route("/dashboard")
def dashboard_page():
    return render_template("dashboard.html")
