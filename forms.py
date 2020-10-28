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
    date = datetime.datetime.now().strftime('%B %d, %Y %I:%M%p')
    time_spent = StringField(
        "Time Spent (ex. 1 hour)",
        [validators.DataRequired("Please enter a value.")]
    )
    what_you_learned = StringField(
        "What You Learned",
        [validators.DataRequired("Please enter what you learned today.")]
    )
    resources_to_remember = StringField(
        "Sources you want to remember", 
        [validators.DataRequired("Please enter a value.")]
    )
    tags = StringField(
        "Separate by comma (,)", 
        [validators.DataRequired("Please enter at least one tag.")]
    )
