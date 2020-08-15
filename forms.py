from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.fields.html5 import URLField


class AddForm(FlaskForm):

    name  = StringField('Name of the Template:')
    actor = StringField('Enter the actor in the Template:')
    movie = StringField('Enter the movie of the Template:')
    link  = URLField   ('Link to the Template:')
    submit = SubmitField('Add Template')

class FindForm(FlaskForm):

    actor = StringField('Actor in the Template:')
    movie = StringField('Movie of the Template:')
    submit = SubmitField('Find Template')
