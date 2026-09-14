#obsahuje definicie formularov
#wtforms = triedy ktore defunju ake polia ma fromular na webe, automaticky generuju html formulare, zabudovana validacia (overenie spravnosti dat)

from flask_wtf import FlaskForm     #FlaskForm  - zakladna trieda ktoru vsetky formulare budu dedit
from wtforms import StringField, PasswordField, SubmitField     #StringField  - textove pole (napr. na meno),   PasswordField - pole pre heslo (skryte znaky)
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional    #validators  - kontroluju ci je pole vyplnene (DataRequired), a ci maju spravnu dlzku
from wtforms import FloatField, SelectField, DateField
from datetime import datetime, timedelta

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Heslo', validators=[DataRequired()])
    submit = SubmitField('Prihlásiť sa')

class RegistrationForm(FlaskForm):      #trieda ktora definuje polia pre registraciu
    username = StringField('Používateľské meno', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Heslo', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Zopakuj heslo', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Zaregistrovať sa')

# formular pre zabudnute heslo
class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Pošli mi nové heslo')

# formular pre nastavenie noveho hesla
class ResetPasswordForm(FlaskForm):
    password = PasswordField('Nové heslo', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Zopakuj nové heslo', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Zmeniť heslo')

class CreateFridgeForm(FlaskForm):
    name = StringField('Názov chladničky', validators=[DataRequired(), Length(min=2, max=100)])
    submit = SubmitField('Vytvoriť chladničku')


class AddItemForm(FlaskForm):       #formular na rpidanie novej polozky
    name = StringField('Názov položky', validators=[DataRequired(), Length(min=1, max=100)])        #stringfield = textove vstupne pole; validators = kontroly: pole musi byt vyplnene a mat 1-100znakov
    quantity = FloatField('Množstvo', validators=[DataRequired()], default=1.0)     #floatdield= pole pre desatine cisla; predvyplnena hodnota 1.0
    notes = StringField('Poznámky', validators=[Length(max=500)])       # tym ze tam nie je data required tak su bez validatora a su iba volitelne
    unit = SelectField('Jednotka', choices=[
        ('ks', 'kusov'),
        ('kg', 'kilogramov'),
        ('g', 'gramov'),
        ('l', 'litrov'),
        ('ml', 'mililitrov'),
        ('balenie', 'balení')
    ], default='ks')        #vyberove polia - selectfield = rozbalovaci zoznam; choices = zoznam moznosti vo formate (hodnota_do_databazy, text_pre_uziv.)
    category = SelectField('Kategória', choices=[
        ('mliečne', 'Mliečne výrobky'),
        ('mäso', 'Mäso a údeniny'),
        ('zelenina', 'Zelenina'),
        ('ovocie', 'Ovocie'),
        ('nápoje', 'Nápoje'),
        ('trvanlivé', 'Trvanlivé potraviny'),
        ('zmrazené', 'Zmrazené'),
        ('ostatné', 'Ostatné')
    ])
    expiry_date = DateField('Dátum spotreby', validators=[Optional()])       #datefield = pole pre vyber datumu; defaukt = automaticky nastavi datum o 7 dni dopredu na spotrebu
    submit = SubmitField('Pridať položku')

class EditItemForm(FlaskForm):
    name = StringField('Názov položky', validators=[DataRequired(), Length(min=1, max=100)])
    quantity = FloatField('Množstvo', validators=[DataRequired()])
    unit = SelectField('Jednotka', choices=[
        ('ks', 'kusov'),
        ('kg', 'kilogramov'),
        ('g', 'gramov'),
        ('l', 'litrov'),
        ('ml', 'mililitrov'),
        ('balenie', 'balení')
    ]) #uz nema default lebo uz upravujem tie hodnoty co uz existuju v databaze
    category = SelectField('Kategória', choices=[
        ('mliečne', 'Mliečne výrobky'),
        ('mäso', 'Mäso a údeniny'),
        ('zelenina', 'Zelenina'),
        ('ovocie', 'Ovocie'),
        ('nápoje', 'Nápoje'),
        ('trvanlivé', 'Trvanlivé potraviny'),
        ('zmrazené', 'Zmrazené'),
        ('ostatné', 'Ostatné')
    ])
    expiry_date = DateField('Dátum spotreby')
    submit = SubmitField('Uložiť zmeny')