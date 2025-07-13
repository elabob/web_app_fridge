from app import create_app, db

app = create_app()

if __name__ == '__main__':
    with app.app_context():     #vutvori databazu len pri prvom spusteni
        db.create_all()

    app.run(debug=True)     #Flask spusti server a bude vypisovat chyby na obrazovku (v rezime debug= True, idealne len pocas vyvoja)
