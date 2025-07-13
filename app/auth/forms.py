#obsahuje definicie formularov

from flask_wtf import FlaskForm     #FlaskForm  - zakladna trieda ktoru vsetky formulare budu dedit
from wtforms import StringField, PasswordField, SubmitField     #StringField  - textove pole (napr. na meno),   PasswordField - pole pre heslo (skryte znaky)
from wtforms.validators import DataRequired, Email, EqualTo, Length     #validators  - kontroluju ci je pole vyplnene (DataRequired), a ci maju spravnu dlzku

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