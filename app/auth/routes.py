from flask import render_template, redirect, url_for, flash, request
from .forms import RegistrationForm, LoginForm, ResetPasswordRequestForm, ResetPasswordForm, CreateFridgeForm
from app.models import User, Fridge, FridgeUser
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from flask_login import login_user, logout_user, login_required, current_user

from flask import Blueprint

main = Blueprint('auth', __name__)

# Domovské stranky
@main.route('/')
def index():
    return render_template("welcome.html")  # uvitacia stranka pre neprihlasenych

@main.route('/sk')
@login_required  # chranene stranky pre prihlasenych
def home_sk():
    return render_template("home_sk.html")

@main.route('/en')
@login_required
def home_en():
    return render_template("home_en.html")

@main.route('/cz')
@login_required
def home_cz():
    return render_template("home_cz.html")

# About sekcie
@main.route('/sk/about')
@login_required
def about_sk():
    return render_template("about_sk.html")

@main.route('/en/about')
@login_required
def about_en():
    return render_template("about_en.html")

@main.route('/cz/about')
@login_required
def about_cz():
    return render_template("about_cz.html")

# Items sekcie
@main.route('/sk/items')
@login_required
def items_sk():
    return render_template("items_sk.html")

@main.route('/en/items')
@login_required
def items_en():
    return render_template("items_en.html")

@main.route('/cz/items')
@login_required
def items_cz():
    return render_template("items_cz.html")

# Login funkcionalita
@main.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            flash('Úspešne prihlásený!', 'success')
            # Zmeň toto na správu používateľov
            return redirect(url_for('auth.user_management'))
        else:
            flash('Nesprávny email alebo heslo.', 'danger')

    return render_template("login.html", form=form)

@main.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash("Tento email sa už používa. Skús iný.", "danger")
            return render_template("register.html", form=form)

        # Vytvor pouzivatela a hashujem heslo
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password_hash=hashed_password,
        )

        db.session.add(new_user)
        db.session.commit()

        flash("Registrácia úspešná! Teraz sa môžeš prihlásiť.", "success")
        return redirect(url_for("auth.login"))

    return render_template("register.html", form=form)

# Logout funkcionalita
@main.route("/logout")
@login_required
def logout():
    logout_user()
    flash('Úspešne odhlásený!', 'info')
    return redirect(url_for('auth.index'))


@main.route("/reset_password_request", methods=["GET", "POST"])
def reset_password_request():
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            # Tu by sa normálne poslal email, ale my len zmeníme heslo na "123456"
            user.set_password("123456")
            db.session.commit()
            flash('Vaše heslo bolo zmenené na: 123456', 'success')
            return redirect(url_for('auth.login'))
        else:
            flash('Email sa nenašiel.', 'danger')

    return render_template("reset_password_request.html", form=form)


@main.route("/reset_password", methods=["GET", "POST"])
def reset_password():
    form = ResetPasswordForm()
    if form.validate_on_submit():
        # Tu by sa normálne overil token, ale my to urobíme jednoducho
        flash('Heslo úspešne zmenené!', 'success')
        return redirect(url_for('auth.login'))

    return render_template("reset_password.html", form=form)


@main.route('/user_management', methods=['GET', 'POST'])
@login_required
def user_management():
    form = CreateFridgeForm()

    if form.validate_on_submit():
        new_fridge = Fridge(        #vytvori novu chladnicku
            name=form.name.data,
            created_by=current_user.id
        )
        db.session.add(new_fridge)
        db.session.commit()

        fridge_user = FridgeUser(       # pridat pouzivatela ako admin
            user_id=current_user.id,
            fridge_id=new_fridge.id,
            role='admin'
        )
        db.session.add(fridge_user)
        db.session.commit()

        flash('Chladnička bola úspešne vytvorená!', 'success')
        return redirect(url_for('auth.user_management'))

    # ziskat vsetky chladnicky pouzivatela
    fridges = db.session.query(Fridge).join(FridgeUser).filter(
        FridgeUser.user_id == current_user.id
    ).all()

    return render_template('user_management.html', form=form, fridges=fridges)


# Detail chaldnicky - zatial zaklad
@main.route('/fridge/<int:fridge_id>')
@login_required
def fridge_detail(fridge_id):
    # overim ci ma pouzivatel pristup k danej chladnicke
    membership = FridgeUser.query.filter_by(
        user_id=current_user.id,
        fridge_id=fridge_id
    ).first()

    if not membership:
        flash('Nemáte prístup k tejto chladničke!', 'danger')
        return redirect(url_for('auth.user_management'))

    fridge = Fridge.query.get_or_404(fridge_id)
    return render_template('fridge_detail.html', fridge=fridge)