from flask import Flask
from config.config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from app import models
    
    db.init_app(app)
    with app.app_context():
        db.create_all()

    from app.routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app
