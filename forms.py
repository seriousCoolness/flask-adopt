from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, IntegerField, URLField, SelectField
from wtforms.validators import Optional, InputRequired, URL, NumberRange
class AddPetForm(FlaskForm):
    """A form for adding pets."""

    pet_name = StringField('Pet Name', validators=[InputRequired()])

    species = SelectField('Species', choices=[('cat','Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')], validators=[InputRequired()])

    photo_url = URLField('Photo URL', validators=[Optional(True), URL()])

    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=30)])

    notes = StringField('Notes', validators=[Optional()])

    available = BooleanField('Availability')

class EditPetForm(FlaskForm):
    """A form for editting pets."""

    photo_url = URLField('Photo URL', validators=[Optional(True), URL()])

    notes = StringField('Notes', validators=[Optional()])

    available = BooleanField('Availability')