from  flask_wtf import  FlaskForm
from wtforms import  StringField , SubmitField
from wtforms.fields.html5 import  DateField

from wtforms.validators import DataRequired

class TeacherForm(FlaskForm):
    name =StringField('Name' , validators=[DataRequired()])
    initials = StringField('Initials' , validators=[DataRequired()])
    dob      = DateField('Date of Birth' )
    submit   = SubmitField("Register")