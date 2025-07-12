#vo Flask aplikacii musim mat tzv tajny kluc, ktory Flask-WTF pouzije na ochranu formularov (tokeny)
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'OUN4KRfj5E0jvt9t'

    from app.auth.routes import main
    app.register_blueprint(main)

    return app