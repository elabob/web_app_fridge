from app import create_app      #volam funkciu ktoru som vytvorila v __init__.py

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)     #Flask spusti server a bude vypisovat chyby na obrazovku (v rezime debug= True, idealne len pocas vyvoja)
