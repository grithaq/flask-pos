from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.widgets import TextInput

class CategoryForm(FlaskForm):
    name = StringField("Name", widget=TextInput())