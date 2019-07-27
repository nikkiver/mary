from flask_wtf import FlaskForm
from wtforms import StringField ,SubmitField , SelectField , FieldList , FormField
from wtforms.fields.html5 import  DateField
from wtforms.validators import DataRequired
from .defaultersform import DefaultersForm

class DefaultersListForm(FlaskForm):
    defaulters = FieldList(FormField(DefaultersForm, "Correspondance"), min_entries=0, max_entries=70)
    submit = SubmitField('Submit')
