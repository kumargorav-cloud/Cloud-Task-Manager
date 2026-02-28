from app import db
from datetime import datetime
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class User(db.Model):
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(100), unique=True, nullable=False)
	email = db.Column(db.String(150), unique=True, nullable=False)
	password_hash = db.Column(db.String(255), nullable=False)
	role = db.Column(db.String(50), default="user")
	created_at = db.Column(db.DateTime, default=datetime.utcnow)

	tasks = db.relationship("Task", backref="owner", lazy=True)

	def set_password(self, password):
		self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

	def check_password(self, password):
		return bcrypt.check_password_hash(self.password_hash, password)

class Task(db.Model):
	__tablename__ = "tasks"

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(200), nullable=False)
	description = db.Column(db.Text)
	status = db.Column(db.String(50), default="pending")
	created_at = db.Column(db.DateTime, default=datetime.utcnow)

	user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
