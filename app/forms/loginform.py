from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField ,SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('User name' , validators=[DataRequired()])
    password =PasswordField('Password' , validators=[DataRequired()])
    submit = SubmitField('Login')