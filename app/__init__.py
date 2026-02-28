
from app.config import Config
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)

    from app.auth import auth_bp
    from app.routes import task_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(task_bp)

    return app
