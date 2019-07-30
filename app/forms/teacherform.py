from  flask_wtf import  FlaskForm
from wtforms import  StringField , SubmitField , PasswordField
from wtforms.fields.html5 import  DateField

from wtforms.validators import DataRequired

class TeacherForm(FlaskForm):
    name =StringField('Name' , validators=[DataRequired()])
    initials = StringField('Initials' , validators=[DataRequired()])
    dob      = DateField('Date of Birth' )
    pno     =StringField('Phone number' )
    password =PasswordField('Create Password' , validators=[DataRequired()])

    submit   = SubmitField("Register")