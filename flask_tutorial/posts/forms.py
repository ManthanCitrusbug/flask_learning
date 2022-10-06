from flask_wtf.file import FileField, FileAllowed
from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField


class AddPost(FlaskForm):
    title = StringField("Title", validators=[validators.Length(min=2, max=70)])
    discription = StringField("Discription", validators=[validators.DataRequired()])
    image = FileField("Image", validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField("Add Post")