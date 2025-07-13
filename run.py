from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all()
    print("Databáza bola aktualizovaná!")

    app.run(debug=True)     #Flask spusti server a bude vypisovat chyby na obrazovku (v rezime debug= True, idealne len pocas vyvoja)
