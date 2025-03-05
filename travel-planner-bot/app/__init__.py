from flask import Flask
from .routes import init_routes
from .models import db

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///travel.db"
    db.init_app(app)
    return app

def create_app():
    app = Flask(__name__)
    init_routes(app)
    return app