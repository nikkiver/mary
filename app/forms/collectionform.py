from flask_wtf import FlaskForm
from wtforms import StringField ,SubmitField , SelectField
from wtforms.fields.html5 import  DateField
from wtforms.validators import DataRequired
from app.models import Subject

class CollectionForm(FlaskForm):
    description =StringField('Description' ,validators=[DataRequired()])
    standard   = SelectField('Standard' , choices=[('VI-A' ,'VI-A'),('VII-A' ,'VII-A'),('VII-B' ,'VII-B')])
    subjects   = SelectField('Subject' ,choices=[(s.title , s.title) for s in Subject.query.order_by('title').all() ])
    doc        = DateField('Date of Collection' )
    teacher    = StringField('Teacher innintials' , validators=[DataRequired()])
    submit     =SubmitField('Create')
    #[(s.title , s.title) for s in Subject.query.order_by('title').all() ]