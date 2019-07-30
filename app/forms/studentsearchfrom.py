from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField ,SubmitField
from wtforms.validators import DataRequired

class StudentSearchForm(FlaskForm):
    admno = StringField('Enter Admission no.' , validators=[DataRequired()])
    submit = SubmitField('Search')