from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField
from wtforms.widgets import TextInput, TextArea

class CategoryForm(FlaskForm):
    name = StringField("Name", widget=TextInput())


class ItemForm(FlaskForm):
    name = StringField("Name", widget=TextInput())
    description = StringField("Description", widget=TextArea())
    price = StringField("Price", widget=TextInput())
    stock = StringField("Stock", widget=TextInput())
    image = FileField("Image",validators=[FileAllowed(['jpg', 'png','ppt','', None])])