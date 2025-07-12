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

@main.route('/cz')
def home_cz():
    return render_template("home_cz.html")


#------------about section

@main.route('/sk/about')
def about_sk():
    return render_template("about_sk.html")

@main.route('/en/about')
def about_en():
    return render_template("about_en.html")

@main.route('/cz/about')
def about_cz():
    return render_template("about_cz.html")

#------------items section

@main.route('/sk/items')
def items_sk():
    return render_template("items_sk.html")

@main.route('/en/items')
def items_en():
    return render_template("items_en.html")

@main.route('/cz/items')
def items_cz():
    return render_template("items_cz.html")