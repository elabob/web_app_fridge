#vo Flask aplikacii musim mat tzv tajny kluc, ktory Flask-WTF pouzije na ochranu formularov (tokeny)
# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.models import db
from app.auth.routes import main

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'OUN4KRfj5E0jvt9t'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()  # vytvori tabulky v databaze pri starte

    return app
