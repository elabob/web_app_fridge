#starter celej aplikacie - flask potrebuje aplokacny kontext- objekt ktory drzi vsetko pokope

from flask import Flask         #importuje triedu flask ktora sluzi na vyvtorenie webovej appky

def create_app():       #vytvaram funkciu ktora mi umozni oddelit inicializaciu appky od spustenia
    app = Flask(__name__)   #tymto vytvorim Flask aplikaciu

    from .routes import main  #nacitanie cesty z ineho suboru  #zaroven tu inicializujem blueprint- sposob ako organizovat cesty do samostatneho modulu

    app.register_blueprint(main)  #pridavam subor main do aplikacie  #zaregistrujem blueprint do aplikacie aby Flask vedel ze su tam definovane trasy (/login,..)

    return app
