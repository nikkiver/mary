from flask_wtf import FlaskForm
from wtforms import StringField ,SubmitField , SelectField
from wtforms.fields.html5 import  DateField
from wtforms.validators import DataRequired
from app.models import  Subject

class StandardSubjectSelectorForm(FlaskForm):
    standard = SelectField('Standard' , choices=[('VI' ,'VI'),('VII' ,'VII'),('VIII' ,'VIII'),('IX' ,'IX'),('X' ,'X')] , validators=[DataRequired()])
    section  =SelectField('Section' , choices=[('A','A'),('B','B'),('C','C'),('D','D')] , validators=[DataRequired()])
    subject  =SelectField('Subject' , choices=[(s.title , s.title) for s in Subject.query.order_by('title').all() ], validators=[DataRequired()])
    submit  = SubmitField('Add Subject')

