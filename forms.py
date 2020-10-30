import datetime

from flask_wtf import Form
from wtforms import StringField, TextAreaField, DateField, validators
from wtforms.validators import DataRequired, Length, ValidationError

from models import Entry
    
    
class EntryForm(Form):
    title = StringField(
        "Title",
        [validators.DataRequired("Please enter a title.")]
    )
    date = DateField(
        "Date",
        [validators.DataRequired("Please enter a date.")]
    )
    time_spent = StringField(
        "Time Spent",
        [validators.DataRequired("Please enter the amount of time spent.")]
    )
    what_you_learned = StringField(
        "What You Learned",
        [validators.DataRequired("Please enter what you learned today.")]
    )
    resources_to_remember = StringField(
        "Resources to Remember", 
        [validators.DataRequired("Please enter at least one resource.")]
    )
    tags = StringField(
        "Tags", 
        [validators.DataRequired("Please enter at least one tag.")]
    )
