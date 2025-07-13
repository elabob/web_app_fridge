#user model -definicia pouzivatela

from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

#aby flask-login pochopil ako ziskat aktualneho prihlaseneho pouzivatela podla jeho ID ulozeneho v session
from app import login_manager

@login_manager.user_loader      #specialny dekoder
def load_user(user_id):     #dostane ID pouzivatela
    return User.query.get(int(user_id))     #vrati objekt pouzivatela z databazy: user.query.get(int(user_id))


class Fridge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)        #db.ForeignKey('user.id') - toto je odkaz na ID pouzivatela
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    # vztah - kto vytvoril chladnicku
    creator = db.relationship('User', backref='created_fridges')        #toto vytvori spojenie medzi tabulkami;     backref umoznuje pristupovat k datam opacnej strany


class FridgeUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    fridge_id = db.Column(db.Integer, db.ForeignKey('fridge.id'), nullable=False)
    role = db.Column(db.String(20), default='member')  # 'admin' alebo 'member'
    joined_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    # vztahy
    user = db.relationship('User', backref='fridge_memberships')
    fridge = db.relationship('Fridge', backref='members')