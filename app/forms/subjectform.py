from flask_wtf import FlaskForm 
from wtforms import StringField ,SubmitField
from wtforms.validators import DataRequired

class SubjectForm(FlaskForm):
    title = StringField('Subject name' , validators=[DataRequired()])
    submit = SubmitField('Create')