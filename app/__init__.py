#vo Flask aplikacii musim mat tzv tajny kluc, ktory Flask-WTF pouzije na ochranu formularov (tokeny)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # presmeruj na login, nie register
login_manager.login_message_category = 'info'  # typ flash spravy
login_manager.login_message = 'Prosím prihláste sa pre prístup k tejto stránke.'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'OUN4KRfj5E0jvt9t'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)

    from .models import User
    from .auth.routes import main as auth_blueprint

    app.register_blueprint(auth_blueprint)

    return app