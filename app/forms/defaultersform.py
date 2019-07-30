from flask_wtf import FlaskForm
from wtforms import StringField ,SubmitField , SelectField , FieldList ,RadioField
from wtforms.fields.html5 import  DateField
from wtforms.validators import DataRequired

class DefaultersForm(FlaskForm):
    admno = StringField('Admno' ,validators=[DataRequired()])
    name  = StringField('Student name' , validators=[DataRequired()])
    status =RadioField('Status' , choices=[('AB','ABSENT'),('NS','NOT SUBMITTED'),('INC' ,'INCOMPLETE WORK') ])