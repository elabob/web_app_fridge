from flask import Blueprint, render_template, redirect, url_for, flash
from app.auth.forms import LoginForm

main = Blueprint('main', __name__)


# Domovské stránky
@main.route('/')
def index():
    return render_template("home_sk.html")


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
@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        if username == "admin" and password == "tajneheslo":
            flash('Úspešne prihlásené!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Nesprávne meno alebo heslo.', 'danger')
    return render_template('login.html', form=form)