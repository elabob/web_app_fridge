from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.auth.forms import LoginForm, RegisterForm
from app.models import db, User
from flask import session

main = Blueprint('main', __name__)


# Domovské stranky
@main.route('/')
def index():
    return render_template("welcome.html")  # nová uvítacia stránka

@main.route('/sk')
def home_sk():
    return render_template("home_sk.html")


@main.route('/en')
def home_en():
    return render_template("home_en.html")


@main.route('/cz')
def home_cz():
    return render_template("home_cz.html")


# About sekcie
@main.route('/sk/about')
def about_sk():
    return render_template("about_sk.html")


@main.route('/en/about')
def about_en():
    return render_template("about_en.html")


@main.route('/cz/about')
def about_cz():
    return render_template("about_cz.html")


# Items sekcie
@main.route('/sk/items')
def items_sk():
    return render_template("items_sk.html")


@main.route('/en/items')
def items_en():
    return render_template("items_en.html")


@main.route('/cz/items')
def items_cz():
    return render_template("items_cz.html")


# Login funkcionalita
@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash('Používateľ už existuje.', 'warning')
            return redirect(url_for('main.register'))

        new_user = User(username=form.username.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Registrácia úspešná. Môžeš sa prihlásiť.', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            session['user'] = user.username
            flash('Úspešne prihlásené!', 'success')
            return redirect(url_for('main.home_sk'))
        else:
            flash('Nesprávne meno alebo heslo.', 'danger')
    return render_template('login.html', form=form)


@main.route('/logout')
def logout():
    session.pop('user', None)
    flash('Bola si odhlásená.', 'info')
    return redirect(url_for('main.login'))