from flask import Blueprint, request, jsonify, session
from app import db, bcrypt
from app.models import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register",methods=["POST"])

def register():
	data = request.get_json()

	username = data.get("username")
	email = data.get("email")
	password = data.get("password")

	if not username or not email or not password:
		return jsonify({"error":"All fields required"}), 400

	if User.query.filter_by(email=email).first():
		return jsonify({"error":"Email already exists"}), 400

	new_user = User(username=username, email=email)
	new_user.set_password(password)

	db.session.add(new_user)
	db.session.commit()

	return jsonify({"message":"User registered successfully"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
	data = request.get_json()

	email = data.get("email")
	password = data.get("password")

	user = User.query.filter_by(email=email).first()

	if not user or not user.check_password(password):
		return jsonify({"error":"Invalid credentials"}), 401

	session["user_id"] = user.id

	return jsonify({"message":"Login successful"}), 200

@auth_bp.route("/logout",methods=["POST"])
def logout():
	session.pop("user_id", None)

	return jsonify({"message":"Logged out"}), 200
