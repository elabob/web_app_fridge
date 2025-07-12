#subor kde budem pisat jednotlive stranky mojej aplikacie

from flask import Blueprint, render_template

main = Blueprint('main', __name__)   #vytvaram blueprint - maly modul aplikacie (main, auth, admin - kazdy so svojimi trasami)

@main.route('/')
def index():
    return render_template("home_sk.html")

@main.route('/sk')    #ked niekto otvori adresu / spusti sa tato funkcia. Zobrazi stranku
def home_sk():
    return render_template("home_sk.html")     #zobrazi HTML sablonu z priecinka tamplates/

@main.route('/en')
def home_en():
    return render_template("home_en.html")