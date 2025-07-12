#obsahuje definicie formularov

from flask_wtf import FlaskForm     #FlaskForm  - zakladna trieda ktoru vsetky formulare budu dedit
from wtforms import StringField, PasswordField, SubmitField     #StringField  - textove pole (napr. na meno),   PasswordField - pole pre heslo (skryte znaky)
from wtforms.validators import InputRequired,Length, EqualTo     #validators  - kontroluju ci je pole vyplnene (DataRequired), a ci maju spravnu dlzku

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=30)])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=30)])
    confirm_password = PasswordField('Confirm Password', validators=[
        InputRequired(), EqualTo('password', message='Passwords must match.')
    ])
    submit = SubmitField('Register')