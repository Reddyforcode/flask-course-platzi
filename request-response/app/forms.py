from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms.fields import StringField, PasswordField, SubmitField

"""
class Loginform(FlaskForm):
    # campo ara username and pass
    username = StringField('Nombre de Usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField("Enviar")
"""

class LoginForm(FlaskForm):
    validators = [DataRequired()]
    username = StringField('Nombre de Usuario', validators=validators)
    password = PasswordField('Password', validators=validators)
    submit = SubmitField('Enviar')