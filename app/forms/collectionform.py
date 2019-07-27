from flask_wtf import FlaskForm
from wtforms import StringField ,SubmitField , SelectField
from wtforms.fields.html5 import  DateField
from wtforms.validators import DataRequired

class CollectionForm(FlaskForm):
    description =StringField('Description' ,validators=[DataRequired()])
    standard   = SelectField('Standard' , choices=[('VI-A' ,'VI-A'),('VII-A' ,'VII-A'),('VII-B' ,'VII-B')])
    doc        = DateField('Date of Collection' )
    teacher    = StringField('Teacher innintials' , validators=[DataRequired()])
    submit     =SubmitField('Create')