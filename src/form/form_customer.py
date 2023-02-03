from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField
from wtforms.widgets import TextInput, TextArea


class CustomerForm(FlaskForm):
    first_name = StringField("First Name", widget=TextInput())
    last_name = StringField("Last Name", widget=TextInput())
    address = StringField("Address", widget=TextArea())
    phone_number = StringField("Phone Number", widget=TextInput())
