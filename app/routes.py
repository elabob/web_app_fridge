#subor kde budem pisat jednotlive stranky mojej aplikacie

from flask import Blueprint, render_template

main = Blueprint('main', __name__)   #vytvaram blueprint - maly modul aplikacie (main, auth, admin - kazdy so svojimi trasami)

@main.route('/')    #ked niekto otvori adresu / spusti sa tato funkcia. Zobrazi stranku
def home():
    return render_template("home.html")     #zobrazi HTML sablonu z priecinka tamplates/